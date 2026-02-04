import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_retail_data(
    n_stores=3,
    n_items=50,
    start_date='2020-01-01',
    end_date='2022-01-01',
    seed=42
):
    """
    Generates a synthetic dataset mimicking the structure of the M5 competition.
    Structure:
    - sales_df: Date, Store_ID, Item_ID, Sales
    - calendar_df: Date, Wm_yr_wk, Weakday, Holiday_Flag
    - prices_df: Store_ID, Item_ID, Wm_yr_wk, Sell_Price
    """
    np.random.seed(seed)
    
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    n_dates = len(dates)
    
    # Generate Sales Data
    records = []
    
    # Store/Item clusters for variety
    # 0: High Vol, 1: Low Vol, 2: Intermittent
    
    print(f"Generating data for {n_stores} stores and {n_items} items over {n_dates} days...")
    
    for store in range(n_stores):
        for item in range(n_items):
            # Base demand
            base_demand = np.random.gamma(shape=2.0, scale=2.0)
            
            # Trend component
            trend = np.linspace(0, np.random.choice([-0.5, 0.5, 1.0]), n_dates)
            
            # Seasonality (Weekly)
            seasonality = np.sin(np.arange(n_dates) * (2 * np.pi / 7)) * np.random.uniform(0.5, 2.0)
            
            # Noise
            noise = np.random.normal(0, np.sqrt(base_demand), n_dates)
            
            # Sales calculation
            # Log-linear modelish: exp(base + trend + seas) + noise
            # Simplified:
            daily_sales = base_demand + trend + seasonality + noise
            daily_sales = np.maximum(daily_sales, 0).astype(int)
            
            # Inject simulated promotions (price drops boost sales)
            is_promo = np.random.choice([0, 1], size=n_dates, p=[0.9, 0.1])
            daily_sales = daily_sales * (1 + is_promo * 0.5) # 50% boost on promo
            
            for d, sale, promo in zip(dates, daily_sales, is_promo):
                records.append({
                    'date': d,
                    'store_id': f'store_{store}',
                    'item_id': f'item_{item}',
                    'sales': int(sale),
                    'is_promo': int(promo)
                })
                
    df = pd.DataFrame(records)
    
    # Add Price (Static per item for simplicity, modulated by promo)
    # in real M5, price changes weekly.
    # Here we simulate price: Base Price - Discount if Promo
    base_prices = {f'item_{i}': np.random.uniform(5.0, 50.0) for i in range(n_items)}
    
    df['sell_price'] = df['item_id'].map(base_prices)
    df.loc[df['is_promo'] == 1, 'sell_price'] *= 0.8 # 20% off
    
    return df

if __name__ == "__main__":
    import os
    os.makedirs("data/raw", exist_ok=True)
    
    print("Generating M5-Lite Synthetic Data...")
    df = generate_retail_data()
    
    output_path = "data/raw/m5_lite_synthetic.parquet"
    df.to_parquet(output_path, index=False)
    
    print(f"DONE. Data generated and saved to {output_path}")
    print(f"Shape: {df.shape}")
    print(df.head())
