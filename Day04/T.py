from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
@app.post("/items/")
async def create_item(item: Item):
    return item
#运行服务   uvicorn 文件名:app --reload
