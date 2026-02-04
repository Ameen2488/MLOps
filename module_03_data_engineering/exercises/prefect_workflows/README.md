# Exercise: Prefect Workflows

**Objective**: define a Flow with two Tasks.

## 📝 Steps

1. Install: `pip install prefect`.
2. Define task `add(a, b)`.
3. Define task `multiply(a, b)`.
4. Create a `@flow` that calls add then multiply.

```python
from prefect import task, flow

@task
def add(x, y):
    return x + y

@task
def multiply(x, y):
    return x * y

@flow
def math_flow():
    # TODO: Connect the tasks
    pass

if __name__ == "__main__":
    math_flow()
```
