# Exercise: FastAPI Demo

**Objective**: Create a Hello World API.

## 📝 Steps

1. Create `app.py`.
2. Define a GET route `/` that returns `{"msg": "Hello"}`.
3. Define a POST route `/sum` that takes `{"a": 1, "b": 2}` and returns 3.
4. Run with `uvicorn`.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: int
    b: int

# TODO: Define Routes
```
