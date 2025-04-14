# features/launch_apps.py
import os
from core.speaker import speak

# Modify these paths according to your system
apps = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",  # Needs path
    "notepad": "notepad.exe",                                            # No path needed
    "vs code": r"C:\Users\91835\AppData\Local\Programs\Microsoft VS Code\Code.exe",  # Needs path
    "calculator": "calc.exe"                                             # No path needed
}


def launch_application(query):
    for app in apps:
        if app in query:
            app_path = apps[app]
            speak(f"Launching {app}")
            os.startfile(app_path)
            print("")
            return
    speak("Sorry, I couldn't find that application.")
