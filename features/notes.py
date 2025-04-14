import os
from datetime import datetime
from core.speaker import speak

# Define where notes will be stored
NOTES_FILE = os.path.join(os.path.expanduser("~"), "Desktop", "jarvis-notes.txt")          

def write_note(content):
    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {content}\n")
    speak("📝 I've saved your note.")
    print(f"Note saved: {content}")

def read_notes():
    if not os.path.exists(NOTES_FILE):
        speak("You don't have any saved notes.")
        return

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.readlines()

    if notes:
        speak("Here are your saved notes:")
        for note in notes[-5:]:  # read last 5 notes only
            speak(note)
            print(note.strip())
    else:
        speak("You don't have any saved notes.")

def clear_notes():
    if os.path.exists(NOTES_FILE):
        os.remove(NOTES_FILE)
        speak("🗑️ All your notes have been deleted.")
    else:
        speak("There are no notes to delete.")
