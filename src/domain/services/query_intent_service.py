def detect_intent(text):
    t = text.lower()

    if "gmv" in t or "gross merchandise" in t:
        return "GMV"

    return "UNKNOWN"
