
---

## 4. `response_model.md`

```markdown
# FastAPI Response Model

A response model defines the structure and type of data returned by an API endpoint.

FastAPI uses Pydantic models to define response models.

## Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    return {
        "username": "john",
        "email": "john@example.com"
    }