# features/get_datetime.py
from datetime import datetime
from core.speaker import speak

def tell_date_time(query):
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    date = now.strftime("%A, %B %d, %Y")
    if "date" in query and "time" in query:
        speak(f"Today is {date} and the time is {time}\n")
    elif "time" in query:
        speak(f"The time is {time}\n")
    elif "date" in query:
        speak(f"Today is {date}\n")
