from core.intent_classifier import classify_intent
from core.command_registry import COMMAND_REGISTRY
from core.intents import Intent
from core.speaker import speak
from core.logger import logger
from core.context import CommandContext
from features.notes import save_note
from core.utils import is_cancel_command 
   
def process_query(query: str, session) -> bool:
    
    #Exit has highest priority
    if query and "exit" in query.lower():
        speak("Shutting down.")
        return False
    
    #Checking pending intent in session context
    if session.pending_intent == Intent.WRITE_NOTE:
        if is_cancel_command(query):
            logger.info("Note writing cancelled by user.")
            session.pending_intent = None
            speak("Note writing cancelled.")
            return True

        logger.info("Handling pending WRITE_NOTE intent.")
        return handle_pending_note(query, session)
    
    intent = classify_intent(query)
    logger.info(f"Resolved intent: {intent}")
    
    if intent == Intent.UNKNOWN:
        speak("I didn't understand that.")
        return True

    if intent == Intent.WRITE_NOTE:
        logger.info("Starting WRITE_NOTE intent.")
        return start_write_note(query, session)

    command = COMMAND_REGISTRY.get(intent)

    if not command:
        speak("I didn't understand that.")
        return True
    
    context = CommandContext(query)
    command(context)
    
    return True

def start_write_note(query, session):
    # remove command words
    content = query.replace("write a note", "").replace("write a", "").strip()

    if content:
        save_note(content)
        speak("Your note has been saved.")
        return True

    session.pending_intent = Intent.WRITE_NOTE
    logger.info("Prompting user for note content.")
    speak("What should I write?")
    return True


def handle_pending_note(query, session):
    session.pending_intent = None

    if not query:
        logger.info("No content provided for note.")
        speak("No note was saved.")
        return True

    logger.info("Saving note from pending intent.") 
    save_note(query)
    speak("Your note has been saved.")
    return True