from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return (
        '''
        Olá mundo!
        Testando aqui

        Num ninho de mafagafos há sete mafagafinhos. Quando a mafagafa gafa, gafam os sete mafagafinhos.

        rsrsrs!

        '''
        )

@app.get("/itens/{id}/{quantidade}")
def homeitem(id: int, quantidade: Union[str, None] = None):
    return {"item_id": id, "quantidade": quantidade}