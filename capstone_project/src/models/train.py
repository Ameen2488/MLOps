import pandas as pd
import lightgbm as lgb
import joblib
import os
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.features.build_features import create_features

def train():
    print("Loading Data...")
    df = pd.read_parquet('data/raw/m5_lite_synthetic.parquet')
    
    print("Generating Features...")
    df_processed = create_features(df)
    
    # Define features
    features = [
        'lag_7', 'lag_14', 'lag_28',
        'rolling_mean_7', 'rolling_mean_28', 
        'month', 'day_of_week', 'is_weekend', 
        'sell_price', 'is_promo'
    ]
    target = 'sales'
    
    # Train on full dataset for production (Prophet/ARIMA methodology)
    # Or Hold-out last 28 days for validation, but for final artifact we usually want all data.
    # We will stick to training on all data up to last date.
    
    print(f"Training LightGBM on {df_processed.shape[0]} rows...")
    train_data = lgb.Dataset(df_processed[features], label=df_processed[target])
    
    params = {
        'objective': 'regression',
        'metric': 'mae',
        'learning_rate': 0.1,
        'num_leaves': 31,
        'verbose': -1,
        'seed': 42
    }
    
    model = lgb.train(params, train_data, num_boost_round=500)
    
    # Save artifacts
    os.makedirs('models', exist_ok=True)
    model.save_model('models/lgb_model.txt')
    joblib.dump(features, 'models/features.pkl')
    
    print("DONE. Model saved to models/lgb_model.txt")

if __name__ == "__main__":
    train()
