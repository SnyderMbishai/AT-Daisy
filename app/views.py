
from fastapi import FastAPI, Request
from fastapi import APIRouter
# from main import app
from app.sms import SMS
from app.ussd import USSD


app_router = APIRouter(tags=["AT"], dependencies=[])


@app_router.post("/test")
async def send_sms(request: Request):
    data = await request.json()
    phone_numbers = data.get("phone_numbers")
    message = data.get("message")
    return SMS().send(phone_numbers, message)

@app_router.post("/ussd")
async def handle_ussd(request: Request):
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    if text == "":
        #main menu
        response = "CON What would you like to do?\n"
        response += "1. Check account details\n"
        response += "2. Check phone number\n"
        response += "3. Send me a cool message"
    elif text == "1":
        #sub menu 1
        response = "CON What would you like to check on your account?\n"
        response += "1. Account number"
        response += "2. Account balance"
    elif text == "2":
        #sub menu 1
        response = "END Your phone number is {}".format(phone_number)
    elif text == "3":
        try:
            #sending the sms
            sms_response = SMS.send("Thank you for going through this tutorial","+254724430065")
            print(sms_response)
        except Exception as e:
            #show us what went wrong
            print(f"Houston, we have a problem: {e}")
    elif text == "1*1":
        #ussd menus are split using *
        account_number = "1243324376742"
        response = "END Your account number is {}".format(account_number)
    elif text == "1*2":
        account_balance = "100,000"
        response = "END Your account balance is USD {}".format(account_balance)
    else:
        response = "END Invalid input. Try again."

    return response


@app_router.get("/monitor-ussd")
async def monitor_ussd(request: Request):
    print("=====")
    return "hello"