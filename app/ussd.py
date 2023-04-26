# class USSD:
#     def handle_at_ussd(text):
#         #1. What's your name?
#         #2. How can we be of assistence? 1.Emergency 2.info 3.Other
#         ##
#         # if 1. -> Emmergency 1. Ambulance 2. Police 3. Case Officer
#                     # 1. -> Make call, plus follow up number + credit
#                     # 2. -> Give police contacts + credit
#                     # 3. -> Number + credit, send sms to case officer
#         # if 2. -> Info 
#                 # Give them link + data
#         # if 3.-> Other
#                 # forward message to a case officer + provide info link


#         if text == "":
#             breakpoint()
#             response  = "CON What would you want to check \n"
#             response += "1. My Account \n"
#             response += "2. My phone number"
#         # if text == "":
#         #     pass
#         # if text == "":
#         #     pass
#         # if text == "":
#         #     pass
#         # if text == "":
#         #     pass
#         # if text == "":
#         #     pass
#         # if text == "":
#         #     pass

# works with both python 2 and 3
from __future__ import print_function

import africastalking
from settings import settings


username = settings.USER_NAME
api_key = settings.API_KEY

africastalking.initialize(username=username, api_key=api_key)
sms = africastalking.SMS

def ussd_callback(request):
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    #ussd logic
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
            sms_response = sms.send("Thank you for going through this tutorial", sms_phone_number)
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
