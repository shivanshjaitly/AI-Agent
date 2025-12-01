import json
import re
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

class LangchainAdapter:

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY not found in .env")

        self.llm = ChatGroq(
            api_key=api_key,
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            temperature=0
        )

        self.prompt = PromptTemplate.from_template("""
You are a finance KPI extraction AI.

Extract intent ONLY as JSON.

Fields:
- kpi: one of [GMV, REVENUE, GROSS_MARGIN, BANK_COST, SUCCESS_RATE]
- months: list of month names (["October"], ["November"]) or []
- year: number or null
- quarter: number 1-4 or null
- period: one of [MONTH, QUARTER, YTD, CURRENT]

Return JSON only:

{{ 
  "kpi": "",
  "months": [],
  "year": null,
  "quarter": null,
  "period": ""
}}

Question: {question}
""")

    def parse(self, question):
        chain = self.prompt | self.llm
        response = chain.invoke({"question": question})

        text = response.content if hasattr(response, "content") else str(response)

        match = re.search(r"\{.*\}", text, re.S)
        if not match:
            raise ValueError("Invalid LLM JSON output")

        return json.loads(match.group())
