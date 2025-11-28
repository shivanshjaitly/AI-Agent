import os
from groq import Groq

def get_first_chat_model():
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    models = client.models.list().data

    # Prefer chat-capable models with large context
    preferred = []
    for m in models:
        mid = m.id.lower()
        if any(x in mid for x in ["chat", "it", "instruct", "mixtral", "llama"]) and "deprecated" not in mid:
            preferred.append(m.id)

    if preferred:
        return preferred[0]

    # Fallback: return any model
    return models[0].id
