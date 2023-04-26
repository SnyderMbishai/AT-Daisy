class USSD:
    def handle_at_ussd(text):
        #1. What's your name?
        #2. How can we be of assistence? 1.Emergency 2.info 3.Other
        ##
        # if 1. -> Emmergency 1. Ambulance 2. Police 3. Case Officer
                    # 1. -> Make call, plus follow up number + credit
                    # 2. -> Give police contacts + credit
                    # 3. -> Number + credit, send sms to case officer
        # if 2. -> Info 
                # Give them link + data
        # if 3.-> Other
                # forward message to a case officer + provide info link


        if text == "":
            breakpoint()
            response  = "CON What would you want to check \n"
            response += "1. My Account \n"
            response += "2. My phone number"
        # if text == "":
        #     pass
        # if text == "":
        #     pass
        # if text == "":
        #     pass
        # if text == "":
        #     pass
        # if text == "":
        #     pass
        # if text == "":
        #     pass
