from typing import Union

from fastapi import FastAPI
from .lib import factoriel_recusrive

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/facto/{n}")
def read_item(n: int):
    return {"n": n, "facto(n)": factoriel_recusrive(n)}