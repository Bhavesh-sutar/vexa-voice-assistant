import os
from datetime import datetime
from core.listener import take_command
from core.speaker import speak
from core.confirmation import voice_confirm
from core.logger import logger

NOTES_FILE = os.path.join(
    os.path.expanduser("~"), "Desktop", "vexa_notes.txt"
)          

def write_note(context):
    speak("What should I write?")
    content = take_command()
    
    if not content:
        speak("No note was saved.")
        return 
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {content}")
        
    speak("Your note has been saved.")
    
def read_notes(context):
    if not os.path.exists(NOTES_FILE):
        speak("You have no notes.")
        return

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.readlines()
        
    if not notes:
        speak("You have no notes.")
        return
    
    speak("Here are your notes")
    for note in notes[-3:]:
        speak(note)

def clear_notes(context):

    if not os.path.exists(NOTES_FILE):
        logger.info("File not found for clearing notes.")
        speak("There are no notes to delete.")
        return
    
    logger.info("Requesting confirmation for clearing notes.")
    if not voice_confirm("Are you sure you want to delete all your notes?"):
        logger.info("User cancelled note deletion.")
        speak("Deletion cancelled.")
        return
    
    logger.info("Clearing all notes.")
    os.remove(NOTES_FILE)
    speak("All notes have been deleted.")