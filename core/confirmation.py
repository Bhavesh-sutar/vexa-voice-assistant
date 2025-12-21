import time
from core.speaker import speak
from core.listener import take_command
from core.logger import logger

def voice_confirm(message):
  speak(message + " Say yes or no. ")
  time.sleep(0.8)
  
  response = take_command(skip_calibration=True)
  
  if not response:
    speak("I didn't get a confirmation.")
    return False

  logger.info(f"Confirmation response: {response}")
  
  return any(word in response for word in ["yes", "sure", "confirm", "yeah"])
