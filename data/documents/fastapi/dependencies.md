
---

## 5. `dependencies.md`

```markdown
# FastAPI Dependencies

FastAPI provides a dependency injection system that allows reusable logic to be shared between API endpoints.

Dependencies can be used for:

- Authentication
- Authorization
- Database connections
- Common parameters
- Validation
- Shared services

## Basic Example

```python
from fastapi import FastAPI, Depends

app = FastAPI()

def common_parameters(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit
    }

@app.get("/items/")
def read_items(
    commons: dict = Depends(common_parameters)
):
    return commons