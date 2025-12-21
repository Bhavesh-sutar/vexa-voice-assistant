from enum import Enum

class Intent(Enum):
  OPEN = "open"
  LAUNCH = "launch"
  JOKE = "joke"
  TIME = "time"
  DATE = "date"
  WRITE_NOTE = "write_note"
  READ_NOTES = "read_notes"
  CLEAR_NOTES = "clear_notes"
  EXIT = "exit"
  UNKNOWN = "unknown"