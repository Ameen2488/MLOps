# Exercise: Spark Processing

**Objective**: Use PySpark to count words (Hello World of Big Data).

## 📝 Steps

1. Install: `pip install pyspark`.
2. Create a text file `words.txt`.
3. Use Spark to count word frequencies.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Create dummy data
data = [("Hello world",), ("Hello Spark",), ("Spark is fast",)]
df = spark.createDataFrame(data, ["text"])

# TODO: Split text into words and count them
# Hint: Use explode() and split()
```
