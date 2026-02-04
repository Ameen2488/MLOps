import pandas as pd
import numpy as np

def create_features(df):
    """
    Generate features for forecasting models.
    Assumes df has columns: date, store_id, item_id, sales, sell_price, is_promo
    """
    df = df.sort_values(['store_id', 'item_id', 'date']).copy()
    
    # Ensure date is datetime
    if not np.issubdtype(df['date'].dtype, np.datetime64):
        df['date'] = pd.to_datetime(df['date'])
    
    # 1. Date Features
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.dayofweek
    df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
    
    # 2. Lag Features (Shifted)
    for lag in [7, 14, 28]:
        df[f'lag_{lag}'] = df.groupby(['store_id', 'item_id'])['sales'].shift(lag)
        
    # 3. Rolling Features (Shifted by 28 days to prevent leakage in 4-week forecast)
    for window in [7, 28]:
        # Using transform for efficiency
        # We shift by 28 days first (our max horizon) then take rolling mean of THAT.
        # This simulates "What was the trend 28 days ago?" which is the last stable info we have for a 28-day forecast.
        df[f'rolling_mean_{window}'] = df.groupby(['store_id', 'item_id'])['sales'].transform(
            lambda x: x.shift(28).rolling(window).mean()
        )
        
    return df.dropna()
