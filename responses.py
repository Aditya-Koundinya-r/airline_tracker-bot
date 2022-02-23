from datetime import datetime

def sampleResponse(input_text):

    userMessage = str(input_text).lower()

    if userMessage in ("hello", "hi", "start",):
        return "HI, WELCOME"


    if userMessage in ("time", "time?"):
        now = datetime.now()
        dateTime = now.strftime("%d/%m/%y, %H:%M")

        return str(dateTime)


    return "HI THIS IS A BOT"