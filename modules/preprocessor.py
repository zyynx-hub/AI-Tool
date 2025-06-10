import re

def preprocess_text(text):
    if not isinstance(text, str):
        return ""

    # kleine letters
    text = text.lower()

    # Verwijder leestekens en rare tekens
    text = re.sub(r'[^\w\s]', '', text)

    # Extra spaties opruimen
    text = re.sub(r'\s+', ' ', text).strip()

    return text