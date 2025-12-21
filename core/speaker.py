import pyttsx3
from core.logger import logger

_engine = pyttsx3.init()
_engine.setProperty("rate", 175)   # sane default rate
_engine.setProperty("volume", 1.0)
logger.info("TTS Engine Initialized/Created")

_is_speaking = False

def speak(text):
    global _is_speaking

    if not text:
        return

    print(f"Vexa: {text}")

    _is_speaking = True
    _engine.say(text)
    _engine.runAndWait()
    _is_speaking = False

def is_speaking():
    return _is_speaking
