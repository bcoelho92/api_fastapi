from typing import Union
from fastapi import FastAPI
from model import Item


app = FastAPI()

@app.get("/item")
async def home(
    id: int,
    name: str,
    idade: int,
):
    return {"ID":id, "name":name, "idade": idade}

'''
A rota abaixo, recebe o ID, e tambe utiliza o model "item" para receber o "name",

retorna o ID e o NOME.

'''

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
