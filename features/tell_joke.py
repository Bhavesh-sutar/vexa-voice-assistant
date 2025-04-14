# features/tell_joke.py
import pyjokes
from core.speaker import speak

def tell_joke():
    
    joke = pyjokes.get_joke()
    speak(joke)
    print("")
