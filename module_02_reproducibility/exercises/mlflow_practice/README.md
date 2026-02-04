# Exercise: MLflow Practice

**Objective**: Log parameters and metrics.

## 📝 Steps

1. Create `experiment.py`.
2. Instrument it with `mlflow`.
3. Log `param1` (alpha) and `metric1` (rmse).
4. Run `mlflow ui` to view it.

```python
import mlflow

if __name__ == "__main__":
    mlflow.set_experiment("practice_exp")
    
    with mlflow.start_run():
        mlflow.log_param("alpha", 0.5)
        mlflow.log_metric("rmse", 0.88)
        print("Run Complete")
```
