from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def read_root():  # 这是一个简单的路由
    return {"Hello": "World"}

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
@app.post("/items/")
async def create_item(item: Item):
    return item
