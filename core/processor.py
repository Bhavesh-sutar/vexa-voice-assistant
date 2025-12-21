from core.intent_classifier import classify_intent
from core.command_registry import COMMAND_REGISTRY
from core.intents import Intent
from core.speaker import speak
from core.logger import logger
from core.context import CommandContext

def process_query(query: str) -> bool:
    intent = classify_intent(query)
    logger.info(f"Resolved intent: {intent}")

    if intent == Intent.EXIT:
        speak("Shutting down.")
        return False

    command = COMMAND_REGISTRY.get(intent)

    if not command:
        speak("I didn't understand that.")
        return True
    
    context = CommandContext(query)
    command(context)
    
    return True
