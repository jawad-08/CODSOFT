import re

_WHITESPACE = re.compile(r"\s+")

def normalize(text: str) -> str:
    """
    Lowercase + collapse whitespace + strip punctuation at ends.
    We keep punctuation inside the text because rules may need it.
    """
    text = text.strip().lower()
    text = _WHITESPACE.sub(" ", text)
    return text
