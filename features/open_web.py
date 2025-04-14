# features/open_web.py
import webbrowser
from core.speaker import speak

# You can add more mappings here
website_map = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "instagram": "https://www.instagram.com",
    "spotify": "https://open.spotify.com/"
}

def open_website(query):
    for site in website_map:
        if site in query:
            url = website_map[site]
            speak(f"Opening {site}")
            webbrowser.open(url)
            print("")
            return
        
    speak("Sorry, I couldn't find that website in my list.\n")
