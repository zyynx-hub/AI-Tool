def match_theme_from_question(question):
    q = question.lower()
    if "frustratie" in q or "probleem" in q or "irritatie" in q:
        return "frustratie"
    elif "wens" in q or "willen" in q or "verbetering" in q:
        return "wens"
    elif "ai" in q:
        return "ai"
    elif "tip" in q or "suggestie" in q or "aanpassing" in q:
        return "verbetering"
    else:
        return "onbekend"

def find_matching_sentences(df, theme_keywords):
    resultaten = []
    for i, row in df.iterrows():
        for col in df.columns:
            text = row[col]
            if any(keyword in text for keyword in theme_keywords):
                resultaten.append(text)
    return resultaten[:10]  # maximaal 5 zinnen als antwoord

def vraag_ai(df, vraag):
    thema = match_theme_from_question(vraag)

    if thema == "frustratie":
        keywords = ["frustratie", "lastig", "traag", "inefficiënt", "vervelend"]
    elif thema == "wens":
        keywords = ["automatiseren", "makkelijker", "wens", "willen", "verbeteren"]
    elif thema == "ai":
        keywords = ["ai", "kunstmatige intelligentie", "automatisch"]
    elif thema == "verbetering":
        keywords = ["suggestie", "tip", "verbetering", "advies"]
    else:
        return "Sorry, ik snap je vraag niet goed. Probeer iets met 'frustratie', 'wens' of 'AI'."

    zinnen = find_matching_sentences(df, keywords)
    if not zinnen:
        return "Ik heb daar niets over gevonden in de data."
    
    antwoord = "Hier zijn wat antwoorden uit de dataset:\n\n"
    antwoord += "\n".join(f"- {zin}" for zin in zinnen)
    return antwoord
