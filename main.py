from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api import api_router
from app.database.db_class import *
from app.database.db import Base
from core.exceptions.simple_exception import SimpleException

app = FastAPI()
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.exception_handler(SimpleException)
async def simple_exception_handler(request: Request, exception: SimpleException):
    if isinstance(exception, SimpleException):
        response_dict = {
            "message": exception.message,
            "status_code": exception.status_code,
        }

        return JSONResponse(
            status_code=exception.status_code,
            content=response_dict,
        )
