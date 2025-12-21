import speech_recognition as sr
from core.logger import logger

recognizer = sr.Recognizer()
MAX_RETRIES = 2

def take_command(skip_calibration=False):
    for attempt in range(MAX_RETRIES + 1):
        try:
            with sr.Microphone() as source:
                logger.info("Listening...")
                if not skip_calibration:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                recognizer.pause_threshold = 0.5
                audio = recognizer.listen(source, timeout=5)

            logger.info("Recognizing speech...")
            query = recognizer.recognize_google(audio, language="en-in")
            logger.info(f"Recognized: {query}")
            return query.lower()

        except sr.UnknownValueError:
            logger.warning(f"Could not understand speech (attempt {attempt+1})")

        except sr.WaitTimeoutError:
            logger.info("User was silent")
            return ""

        except sr.RequestError as e:
            logger.error(f"Speech service error: {e}")
            return ""

        except Exception as e:
            logger.error(f"Microphone error: {e}")
            return ""

    logger.warning("Max retries exceeded")
    return ""
