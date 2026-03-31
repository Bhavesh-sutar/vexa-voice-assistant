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
    
    text = text.lower().strip() # Lower text and remove leading and trailing with spaces
    
    for phrase in PHRASES_FILLER:
      text = re.sub(rf"\b{phrase}\b", "", text) #Remove the useless phrases from query using regex
    
    tokens = text.split() # Make a list of query words/tokens
    
    tokens = [t for t in tokens if t not in FILLER_WORDS] #Remove filler words from query tokens and make a new list without filler words
    
    return " ".join(tokens) # Join the Query tokens with a space in between and return as string