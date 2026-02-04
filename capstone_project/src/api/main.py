from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import lightgbm as lgb
import joblib
import pandas as pd
import numpy as np
import os

app = FastAPI(title="Retail Pulse API", version="1.0")

# Global variables for artifacts
model = None
features_list = None
mock_db = None # Simulating a database of recent history

def load_artifacts():
    global model, features_list, mock_db
    if os.path.exists("models/lgb_model.txt"):
        model = lgb.Booster(model_file="models/lgb_model.txt")
        features_list = joblib.load("models/features.pkl")
        
        # Load a snippet of data to act as our "Recent History DB" for lag generation
        full_df = pd.read_parquet("data/raw/m5_lite_synthetic.parquet")
        mock_db = full_df.tail(60 * 50 * 3) # Last 60 days for all items
        print("DONE. Models and DB loaded.")
    else:
        print("WARNING: Model content not found. Run python src/models/train.py first.")

@app.on_event("startup")
async def startup_event():
    load_artifacts()

class ForecastRequest(BaseModel):
    store_id: str
    item_id: str
    days: int = 14

@app.post("/forecast")
def get_forecast(request: ForecastRequest):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    # In a real batch system, we would just read from SQL: SELECT * FROM forecasts WHERE ...
    # Here, we simulate "On-Demand" inference using the Batch Model for demonstration.
    
    # 1. Get recent history for this item
    history = mock_db[(mock_db['store_id'] == request.store_id) & 
                      (mock_db['item_id'] == request.item_id)].copy()
    
    if history.empty:
        raise HTTPException(status_code=404, detail="Item history not found")
        
    # 2. Create Future DataFrame
    last_date = history['date'].max()
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=request.days)
    
    future_df = pd.DataFrame({
        'date': future_dates,
        'store_id': request.store_id,
        'item_id': request.item_id,
        'sales': np.nan, # Unknown
        'is_promo': 0, # Assume no promo for future (or pass in request)
        'sell_price': history['sell_price'].iloc[-1] # Assume price stays same
    })
    
    # 3. Append to history to form Rolling Window Context
    eval_df = pd.concat([history, future_df], axis=0).reset_index(drop=True)
    
    # 4. Feature Engineering (Re-using our pipeline code would be best, here we inline simplified version)
    # We need to recreate lags. Since we don't know future sales, calculating lag_7 for day+8 is separate problem (Recursive).
    # FOR SIMPLICITY: We assume 'Direct Strategy' where we only predict horizons where lags exist or use static lags.
    # Actually, simpler: We only return the prediction for Day+1 to Day+7 where Feature Generation is safe-ish.
    
    # Re-running build_features on the fly
    from src.features.build_features import create_features
    processed = create_features(eval_df)
    
    # Filter for the future rows
    future_feat = processed[processed['date'] > last_date]
    
    if future_feat.empty:
        return {"error": "Not enough history to generate features for future"}
        
    preds = model.predict(future_feat[features_list])
    
    return {
        "store_id": request.store_id,
        "item_id": request.item_id,
        "forecast": [
            {"date": d.strftime("%Y-%m-%d"), "sales": float(p)}
            for d, p in zip(future_feat['date'], preds)
        ]
    }

@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": model is not None}
