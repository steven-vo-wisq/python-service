from fastapi import APIRouter, HTTPException
from app.models.models import Item, ItemCreate

router = APIRouter(prefix="/api")

# Simulated database
items_db = {}
item_id_counter = 0

@router.post("/items/", response_model=Item, status_code=201, tags=["items"])
def create_item(item: ItemCreate):
    global item_id_counter
    item_id_counter += 1
    item_dict = item.dict()
    items_db[item_id_counter] = item_dict
    return {"id": item_id_counter, **item_dict}

@router.get("/items/{item_id}", response_model=Item, tags=["items"])
def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items_db[item_id]}