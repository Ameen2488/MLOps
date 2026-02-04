# Exercise: Hyperparameter Search

**Objective**: Tune a Random Forest using Optuna.

## 📝 Steps

1. Install `optuna scikit-learn`.
2. Load Diabetes dataset.
3. Define objective to tune `n_estimators` (10-100) and `max_depth` (1-10).
4. Run 20 trials.

```python
import optuna
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

def objective(trial):
    # TODO: Define params
    # n_estimators = ...
    # max_depth = ...
    
    model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth)
    return cross_val_score(model, X, y, cv=3).mean()
```
