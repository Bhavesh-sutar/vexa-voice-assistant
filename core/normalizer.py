import re

FILLER_WORDS = [ "please", "um", "uh", "like", "you know", "so", "actually", "basically", "right", "hey", "hello", "kindly"]

PHRASES_FILLER = [
  "could you",
  "can you",
  "you know",
  "i mean"
]

def normalize_command(text):
    if not text:
      return ""
    
    text = text.lower().strip()
    
    for phrase in PHRASES_FILLER:
      text = re.sub(rf"\b{phrase}\b", "", text)
    
    tokens = text.split()
    
    tokens = [t for t in tokens if t not in FILLER_WORDS]
    
    return " ".join(tokens)