import os
import json
from flask import Flask, request
import africastalking

app = Flask(__name__)
from dotenv import load_dotenv
load_dotenv()

response = ""
breakpoint()

africastalking.initialize(username=os.getenv("USER_NAME"), api_key=os.getenv("API_KEY"))
af_sms_client = africastalking.SMS

@app.route('/api/send-sms', methods=['POST'])
def send_sms():
    try:
        data = json.loads(request.data)
        phone_numbers = data.get("phone_numbers")
        message = data.get("message")
        response = af_sms_client.send(message, phone_numbers)
    except Exception as e:
        print("=====", str(e))
        return {f"ERROR: {str(e)}"}
    return response

@app.route('/api/ussd', methods=['POST', 'GET'])
def ussd_callback():
    try:
        global response
        session_id = request.values.get("sessionId", None)
        service_code = request.values.get("serviceCode", None)
        phone_number = request.values.get("phoneNumber", None)
        text = request.values.get("text", "default")
        if text == "":
            response += "CON How can we be of assistance?\n"
            response += "1. Emergency\n"
            response += "2. Information\n"
            response += "3. Other\n"
        elif text == "1":
            response = "CON Pick an option\n"
            response += "1. Ambulance\n"
            response += "2. Police\n"
            response += "3. Case officer\n"
        elif text == "1*1":
            response = "END Call this number +25476543290, \n we have awarded you some credit."
        elif text == "1*2":
            response = "END Call this number 072456743 to speak to an officer, \n we have awarded you some credit to use."
        elif text == "1*3":
            response = "END Call 0756786r4 to speak to a case officer. \n we have awarded you some credit"
            response=""
        elif text == "2":
            response = "END https://www.onebillionrising.org/48487/v-day-safe-house-for-the-girls-in-kenya-celebrates-20-years-of-combatting-fgm-changing-culture-educating-girls/"
        elif text == "3":
            response = "END Case forwarded to case officer\n"
        return response
    except Exception as e:
        print("======", str(e))
        return str(e)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT', 8000))
