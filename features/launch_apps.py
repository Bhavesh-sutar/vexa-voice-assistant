# features/launch_apps.py
import os
from core.speaker import speak

# Modify these paths according to your system
APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "vs code": r"C:\Users\91835\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "calculator": "calc.exe"
}


def launch_application(context):
    query = context.raw_query
    for app, path in APPS.items():
        if app in query:
            speak(f"Launching {app}")
            os.startfile(path)
            return
        
    speak("I couldn't find that application.")
