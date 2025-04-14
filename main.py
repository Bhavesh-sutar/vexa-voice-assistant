# main.py
import time
from core.speaker import speak
from core.listener import take_command
from core.processor import process_query

def greet():
    speak("Hello Sir, how can I help you now.")

def main():
    greet()
    while True:
        query = take_command().lower()
        process_query(query)

if __name__ == "__main__":
    main()
