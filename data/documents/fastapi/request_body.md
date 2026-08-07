
---

## 3. `request_body.md`

```markdown
# FastAPI Request Body

A request body contains data sent by the client to the API.

FastAPI commonly uses Pydantic models to define and validate request bodies.

## Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

@app.post("/items/")
def create_item(item: Item):
    return item