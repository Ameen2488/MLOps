# 🛒 Capstone Plan: "Retail Pulse" - SOTA Demand Forecasting System

**Goal**: Build an industry-grade, multi-product demand forecasting platform that compares and deploys four distinct modeling approaches (Statistical, Prophet, Tree-based, Deep Learning) to solve real-world inventory challenges.

## ⚙️ User Configuration
*   **Inference Strategy**: **Batch (Nightly)**. We will pre-compute forecasts for the next horizon and cache them.
*   **Dataset**: **M5-Lite (Subset)**. We will use a curated/sampled version of the M5 dataset to respect the CPU-only constraint while maintaining hierarchical complexity.
*   **Compute**: **CPU Only**. Deep Learning models (TFT) will be trained on a smaller subset or with reduced hyperparameters to ensure feasibility.

---

## 🏗️ System Architecture

### 1. Data Pipeline (The "Industrial" Feature Engineering)
Forecasting models live and die by their features. We will build a pipeline that generates:
*   **Target Transformations**: Log/Box-Cox for stability.
*   **Lag Features**: `sales_lag_7d`, `sales_lag_28d`, `sales_lag_365d`.
*   **Rolling Window Statistics**: `mean_7d`, `std_28d`, `skew_7d` (Stability metrics).
*   **Calendar Features**: `is_weekend`, `month_sin/cos` (Cyclical encoding), `days_to_next_holiday`.
*   **Event Features**: `is_promotion_active`, `price_change_indicator`.
*   **Static Covariates**: `store_id`, `item_category`, `store_location_cluster`.

### 2. Model Zoo (The "Comparison")
We will implement 4 classes of models to understand their Deployment Trade-offs:

| Model Type | Representative | Pros in SOTA | Cons in SOTA | Deployment Challenge |
| :--- | :--- | :--- | :--- | :--- |
| **Statistical** | **AutoARIMA / ETS** (StatsForecast) | Robust, almost no tuning, extremely fast for small N. | Fails on complex external features (price, weather). No cross-learning between items. | **Scalability**: Training 100k models serially is slow. Needs parallelization (Ray/Spark). |
| **Explainable** | **Prophet** (Facebook) | Handling holidays/changepoints is native. Very explainable to business stakeholders. | Computationally heavy per series. Accuracy often beats by GBMs. | **Latency**: Inference is slow. Container size is large. |
| **Tabular SOTA** | **LightGBM / XGBoost** | Global model (learns across items). Handles exogenous features best. Fast training. | Needs heavy feature engineering (Recursive forecasting for multi-step). | **Feature Drift**: Highly sensitive to feature pipelines breaking. |
| **Deep Learning** | **TFT (Temporal Fusion Transformer)** | State-of-the-Art accuracy for complex dependencies. Interpretability (Attention weights). | Data hungry. Hard to tune. Slowest to train. | **Resources**: Needs GPU for training. Inference is heavy (matrix mults). |

### 3. MLOps & Deployment
*   **Experiment Tracking**: MLflow to log MAE/WAPE (Weighted Abs % Error) for all 4 approaches.
*   **Serving**:
    *   **Strategy**: "Batch-Precompute". Real-time forecasting is rare for inventory. We typically forecast the next 14 days every night.
    *   **API**: FastAPI endpoint that serves the *pre-computed* forecast from a Redis/SQL cache (Simulating low-latency reads).
*   **Drift**: Monitoring "Forecast vs Actual" validation and "Feature Drift" (e.g., did we stop running promotions?).

---

## 📅 Implementation Roadmap

### Phase 1: Data Engine (Days 1-3)
- [ ] **Data Ingestion**: Download M5-Lite (Subset of Walmart dataset: 1 State, 3 Categories).
- [ ] **Feature Engineering**: Build `FeatureGenerator` class using Pandas/Polars for speed.
- [ ] **Splitting**: Implementing "Time Series Cross-Validation" (Rolling Origin), not random shuffle.

### Phase 2: Model Development (Days 4-8)
- [ ] **Baseline (Stats)**: Implement `StatsForecast` pipeline.
- [ ] **Prophet**: Implement `Prophet` loop with holiday regressors.
- [ ] **GBM (LightGBM)**: Transform data to tabular format (X, y pairs) and train Global Model.
- [ ] **Deep Learning (TFT)**: Use `PyTorch Forecasting` library to train TFT.
- [ ] **Evaluation**: Compare WAPE across all models.

### Phase 3: Productionization (Days 9-12)
- [ ] **Inference Pipeline**: Script to load best model -> predict next 14 days -> save to DB.
- [ ] **API**: `GET /forecast/{item_id}` endpoint.
- [ ] **Docker**: Containerize the training and inference services separately.

### Phase 4: Monitoring & "The Problems" (Days 13-14)
- [ ] **Simulate Degradation**: Introduce a "shock" (e.g., Competitor price drop) and see which model adapts.
- [ ] **Retraining Trigger**: Dashboard showing Error Rate over time.

---

## 🛠 Tech Stack
*   **Language**: Python 3.9+
*   **Data**: Pandas, Polars (for speed)
*   **Modeling**:
    *   `statsforecast` (Nixla)
    *   `prophet`
    *   `lightgbm`
    *   `pytorch-forecasting` (TFT)
*   **Tracking**: MLflow
*   **Serving**: FastAPI, Docker
