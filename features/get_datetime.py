from datetime import datetime
from core.speaker import speak
from core.intents import Intent

def tell_date_time(context):
    
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    date = now.strftime("%A, %B %d, %Y")
    
    if context.intent == Intent.TIME:
        speak(f"The time is {time}.")
    elif context.intent == Intent.DATE:
        speak(f"Today is {date}.")
        