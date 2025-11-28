import json
import re
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from utils.groq_models import get_first_chat_model

load_dotenv(dotenv_path=".env")

class LangchainAdapter:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY not found in .env")

        model = get_first_chat_model()
        print("✅ Using Groq model:", model)

        self.llm = ChatGroq(
            api_key=api_key,
            model=model,
            temperature=0
        )

        self.prompt = PromptTemplate.from_template("""
You are a finance query understanding AI.

Extract structured meaning strictly as JSON.

Return ONLY JSON:

{{ 
  "metric": "",
  "months": [] 
}}

User Question: {question}
""")

    def parse(self, question):
        chain = self.prompt | self.llm
        response = chain.invoke({"question": question})
        text = response.content if hasattr(response, "content") else str(response)

        match = re.search(r"\{.*\}", text, re.S)
        if not match:
            raise ValueError(f"Invalid LLM output: {text}")

        return json.loads(match.group())
