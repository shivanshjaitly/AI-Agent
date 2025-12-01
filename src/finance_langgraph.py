from typing import TypedDict, List
from langgraph.graph import StateGraph, END

from src.adapters.langchain_adapter import LangchainAdapter
from src.adapters.database_adapter import DatabaseAdapter
from src.domain.services.query_builder_service import build_query
from src.domain.services.result_formatter_service import format_result


class AgentState(TypedDict, total=False):
    question: str
    parsed: dict
    query: str
    result: float
    response: str



def normalize_months(months):
    month_map = {
        "january": 1, "february": 2, "march": 3,
        "april": 4, "may": 5, "june": 6,
        "july": 7, "august": 8, "september": 9,
        "october": 10, "november": 11, "december": 12
    }

    numeric = []
    for m in months or []:
        if isinstance(m, int):
            numeric.append(m)
        elif isinstance(m, str):
            m = m.strip().lower()
            if m in month_map:
                numeric.append(month_map[m])

    return numeric


def nlp_node(state: AgentState) -> AgentState:
    parser = LangchainAdapter()
    parsed = parser.parse(state["question"])

    # ✅ Convert month names → numbers
    parsed["months"] = normalize_months(parsed.get("months", []))

    return {**state, "parsed": parsed}




def normalize_node(state: AgentState) -> AgentState:
    return {
        **state,
        "months": normalize_months(state.get("months", []))
    }


def sql_node(state: AgentState) -> AgentState:
    query = build_query(state["parsed"])
    return {**state, "query": query}



def db_node(state: AgentState) -> AgentState:
    db = DatabaseAdapter()
    return {
        **state,
        "result": db.run(state["query"])
    }


def format_node(state: AgentState) -> AgentState:
    kpi = state["parsed"]["kpi"]
    response = format_result(kpi, state["result"])
    print("FINAL:", response)
    return {**state, "response": response}



builder = StateGraph(AgentState)

builder.add_node("NLP", nlp_node)
builder.add_node("Normalize", normalize_node)
builder.add_node("SQL", sql_node)
builder.add_node("DB", db_node)
builder.add_node("Format", format_node)

builder.set_entry_point("NLP")
builder.add_edge("NLP", "Normalize")
builder.add_edge("Normalize", "SQL")
builder.add_edge("SQL", "DB")
builder.add_edge("DB", "Format")
builder.add_edge("Format", END)
graph = builder.compile()
print("\n📈 LANGGRAPH STRUCTURE:\n")

edges = [
    ("NLP", "Normalize"),
    ("Normalize", "SQL"),
    ("SQL", "DB"),
    ("DB", "Format")
]

for a, b in edges:
    print(f"{a}  --->  {b}")


if __name__ == "__main__":
    while True:
        q = input("Ask Finance Bot (Graph Mode) > ")
        if q.lower() == "exit":
            break
        graph.invoke({"question": q})
