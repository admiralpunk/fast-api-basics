from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

inventory = {
    1: {"name": "Milk", "price": 3.99 , "brand": "Regular"},
    2: {"name": "Bread", "price": 2.99, "brand": "Regular"},
    3: {"name": "Eggs", "price": 1.99, "brand": "Regular"},
}


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., description="The ID of the item you want to view")):
    return inventory[item_id]

#query params
@app.get("/get-by-name")
def get_item_by_name(name: Optional[str] = None):
    for id in inventory:
        if inventory[id]["name"] == name:
            return inventory[id]
    return {"Error": "Item name not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    inventory[item_id] = item
    return inventory[item_id]

