from core.intents import Intent
from core.logger import logger

def classify_intent(text: str) -> Intent:
    if not text:
        return Intent.UNKNOWN

    text = text.lower()

    if text.startswith("open"):
        return Intent.OPEN
    if text.startswith("launch"):
        return Intent.LAUNCH
    if "joke" in text:
        return Intent.JOKE
    if "time" in text:
        return Intent.TIME
    if "date" in text:
        return Intent.DATE
    if "write" in text and "note" in text:
        return Intent.WRITE_NOTE
    if "read" in text and "note" in text:
        return Intent.READ_NOTES
    if "clear" in text or "delete notes" in text:
        return Intent.CLEAR_NOTES
    if text in ("exit", "quit", "stop"):
        return Intent.EXIT

    logger.warning(f"Intent not matched: {text}")
    return Intent.UNKNOWN
