from typing import Union

from fastapi import FastAPI
from app.views import app_router

app = FastAPI()

app.include_router(app_router, prefix="/api")


@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.post("/test")
# def send_sms():
#     breakpoint()
#     return SMS().send(phone_numbers=["0724430065"])

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
