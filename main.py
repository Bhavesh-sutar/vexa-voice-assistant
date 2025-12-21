from core.speaker import speak
from core.listener import take_command
from core.processor import process_query
from core.normalizer import normalize_command
from core.logger import logger

def greet():
    speak("Assistant ready. What can I do?")

def main():
    greet()
    running = True
    while running:
        query = take_command()
        logger.info(f"Query received: {query}")
        query = normalize_command(query)
        logger.info(f"Normalized query: {query}")
        running = process_query(query)
        logger.info(f"Processing Completed for query: {query}")

if __name__ == "__main__":
    logger.info("Vexa Started...")
    main()
