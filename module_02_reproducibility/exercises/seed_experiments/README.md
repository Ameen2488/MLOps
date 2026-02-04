# Exercise: Seed Experiments

**Objective**: meticulous reproducibility.

## 📝 Steps

1. Create a python script `train.py` that trains a simple SVC on Iris.
2. Run it twice. Do you get the *exact* same accuracy?
3. Add `random_state=42` to test split and model.
4. Run it twice. confirming exact match.

```python
# train.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
# TODO: Fix reproducibility here
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = SVC()
model.fit(X_train, y_train)
print(f"Accuracy: {accuracy_score(y_test, model.predict(X_test))}")
```
