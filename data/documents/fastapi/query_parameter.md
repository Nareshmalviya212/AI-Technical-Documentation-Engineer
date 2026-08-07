
---

## 2. `query_parameters.md`

```markdown
# FastAPI Query Parameters

Query parameters are values added to a URL after the question mark.

For example:

/items/?skip=0&limit=10

FastAPI automatically recognizes function parameters that are not part of the path as query parameters.

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit
    }