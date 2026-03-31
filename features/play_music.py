import webbrowser
import requests
from urllib.parse import quote
from core.speaker import speak
from core.logger import logger

def play_music(context):
    query = context.raw_query

    # Extract song name
    song = query.replace("play", "").strip()

    if not song:
        speak("What would you like me to play?")
        return

    logger.info(f"Playing music: {song}")
    speak(f"Playing {song}")

    try:
        search_query = quote(song)
        url = f"https://www.youtube.com/results?search_query={search_query}"

        # Fetch search page
        response = requests.get(url)
        html = response.text

        # Extract first video ID
        video_id_index = html.find("watch?v=")
        video_id = html[video_id_index:video_id_index+20].split('"')[0]

        video_url = f"https://www.youtube.com/{video_id}"

        webbrowser.open(video_url)

    except Exception as e:
        logger.error(f"Error playing music: {e}")
        speak("Sorry, I couldn't play the music.")