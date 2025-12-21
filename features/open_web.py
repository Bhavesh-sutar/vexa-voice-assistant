import webbrowser
from core.speaker import speak

WEBSITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "instagram": "https://www.instagram.com",
    "spotify": "https://open.spotify.com/"
}

def open_website(context):
    query = context.raw_query
    for site, URL in WEBSITES.items():
        if site in query:
            speak(f"Opening {site}")
            webbrowser.open(URL)
            return
        
    speak("I couldn't find that website in my list.")
