# from fastapi.responses import PlainTextResponse
# import africastalking #.Ussd import UssdHandler

from fastapi import FastAPI, Request
from fastapi import APIRouter
# # from main import app
# from app.sms import SMS
# # from app.ussd import USSD


# app_router = APIRouter(tags=["AT"], dependencies=[])
# ussdHandler = africastalking.USSD


# @app_router.post("/test")
# async def send_sms(request: Request):
#     data = await request.json()
#     phone_numbers = data.get("phone_numbers")
#     message = data.get("message")
#     return SMS().send(phone_numbers, message)

# @app_router.post("/ussd")
# async def handle_ussd(request: Request):
#     print("===hits, request.values")
#     breakpoint()
#     x = await request.json()
#     session_id = request.values.get("sessionId", None)
#     service_code = request.values.get("serviceCode", None)
#     phone_number = request.values.get("phoneNumber", None)
#     text = request.values.get("text", "default")
#     if text == "1":
#         #main menu
#         response = "CON What would you like to do?\n"
#         response += "1. Check account details\n"
#         response += "2. Check phone number\n"
#         response += "3. Send me a cool message"


# @app_router.get("/monitor-ussd")
# async def monitor_ussd(request: Request):
#     print("=====")
#     return "hello"

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import africastalking

x = africastalking.USSD

app = FastAPI()
app_router = APIRouter(tags=["AT"], dependencies=[])

@app_router.post("/ussd")
async def ussd_handler(request: Request):
    # Extract relevant USSD data from the request
    breakpoint()
    x = await request.json()
    phone_number = request.phone_number
    session_id = request.session_id
    service_code = request.service_code
    text = request.text

    # Start a new USSD session if this is the first request
    if text == "":
        response_text = "Welcome to Pizza Palace. Choose an option:\n1. Place an order\n2. Track an order\n3. Contact us"
        response = {
            "text": response_text,
            "session_id": session_id,
            "end_of_session": False,
        }
    else:
        # Process the user's input based on the current USSD session state
        if text == "1":
            response_text = "What would you like to order?"
        elif text == "2":
            response_text = "Enter your order ID:"
        elif text == "3":
            response_text = "Call us on +254123456789 or email us at info@pizzapalace.com"
        else:
            response_text = "Invalid input. Please try again."

        response = {
            "text": response_text,
            "session_id": session_id,
            "end_of_session": False,
        }

    return PlainTextResponse(str(response))
