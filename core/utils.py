from core.logger import logger

def is_cancel_command(query: str) -> bool:
    logger.info("In is_cancel_command utility.")
    if not query:
      return False
    query = query.lower().strip()
    return query in ("cancel", "stop", "never mind", "abort")
