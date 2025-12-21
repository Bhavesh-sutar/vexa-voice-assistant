import pyjokes
from core.speaker import speak

def tell_joke(context):
    joke = pyjokes.get_joke()
    speak(joke)
