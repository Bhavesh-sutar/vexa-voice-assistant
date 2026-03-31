import speech_recognition as sr
from core.logger import logger

recognizer = sr.Recognizer()

def take_command(skip_calibration=False):
    try:
        with sr.Microphone() as source:
            logger.info("Listening...")
            if not skip_calibration:
                recognizer.adjust_for_ambient_noise(source, duration=1)
            recognizer.pause_threshold = 0.5
            audio = recognizer.listen(source, timeout=3)

        logger.info("Recognizing speech...")
        query = recognizer.recognize_google(audio, language="en-in")
        logger.info(f"Recognized: {query}")
        return query.lower()

    except sr.UnknownValueError:
        logger.warning(f"Could not understand speech.")

    except sr.WaitTimeoutError:
        logger.info("User was silent")
        return ""

    except sr.RequestError as e:
        logger.error(f"Speech service error: {e}")
        return ""

    except Exception as e:
        logger.error(f"Microphone error: {e}")
        return ""

