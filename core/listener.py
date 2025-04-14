# core/listener.py
import speech_recognition as sr

def take_command():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1  # Wait a bit for the user to speak
            audio = recognizer.listen(source)
    except KeyboardInterrupt:
        print("Program Terminated by user(Keyboard Interrupt)")
        exit()

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn’t catch that.\n")
        return ""
    except sr.RequestError:
        print("Could not connect to the speech recognition service.\n")
        return ""
