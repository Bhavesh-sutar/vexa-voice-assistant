# core/processor.py
import time
from core.speaker import speak
from core.listener import take_command
from features.open_web import open_website
from features.launch_apps import launch_application
from features.tell_joke import tell_joke
from features.get_datetime import tell_date_time
from features.notes import write_note, read_notes, clear_notes

def process_query(query):
    if query == "":
        return
    elif "open" in query:
        open_website(query)
    elif "launch" in query:
        launch_application(query)
    elif "joke" in query:
        tell_joke()
    elif "time" in query or "date" in query:
        tell_date_time(query)
    elif "write a note" in query or "make a note" in query:
        speak("What should I write?")
        note = take_command()
        write_note(note)
    elif "read notes" in query or "show notes" in query:
        read_notes()
    elif "delete notes" in query or "clear notes" in query:
        clear_notes()
    elif "exit" in query or "quit" in query:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I'm not sure how to help with that.")
    time.sleep(1)
