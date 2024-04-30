from fastapi import FastAPI
from app.api import api_router
from app.database.db_class import *
from app.database.db import Base

app = FastAPI()
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
