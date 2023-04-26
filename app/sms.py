# works with both python 2 and 3
from __future__ import print_function

import africastalking
from settings import settings


class SMS:
    def __init__(self):
        self.username = settings.USER_NAME
        self.api_key = settings.API_KEY

        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS

    def send(self, phone_numbers, message):
        recipients = phone_numbers
        message = message

        sender = settings.SENDER
        try:
            response = self.sms.send(message, recipients)
            print(response)
        except Exception as e:
            print("Encountered an error while sending: %s" % str(e))
            # debugger
