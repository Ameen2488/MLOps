# Exercise: Build ETL Pipeline

**Objective**: Create a script that Extracts from CSV, Transforms (cleans), and Loads to Parquet.

## 📝 Steps

1. **Extract**: Read `raw_data.csv` (Simulate with random data).
2. **Transform**: Remove rows where `age < 18`. Normalize `income` (divide by max).
3. **Load**: Save to `cleaned_data.parquet`.

```python
import pandas as pd
import numpy as np

# 1. Simulate Raw Data
df = pd.DataFrame({
    'age': np.random.randint(10, 80, 100),
    'income': np.random.randint(20000, 100000, 100)
})
df.to_csv("raw.csv", index=False)

# TODO: Write your ETL logic below
```
