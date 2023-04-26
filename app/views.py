
from fastapi import FastAPI, Request
from fastapi import APIRouter
# from main import app
from app.sms import SMS


app_router = APIRouter(tags=["AT"], dependencies=[])


@app_router.post("/test")
async def send_sms(request: Request):
    data = await request.json()
    phone_numbers = data.get("phone_numbers")
    message = data.get("message")
    return SMS().send(phone_numbers, message)

