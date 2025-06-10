def detect_theme(text):
    if any(word in text for word in ["frustratie", "lastig", "tijdrovend"]):
        return "Frustratie"
    elif any(word in text for word in ["automatiseren", "verbetering", "efficiënter"]):
        return "Wens"
    elif "ai" in text:
        return "Perceptie AI"
    elif any(word in text for word in ["tip", "suggestie", "aanpassing"]):
        return "Verbeterinitiatief"
    else:
        return "Onbekend"
