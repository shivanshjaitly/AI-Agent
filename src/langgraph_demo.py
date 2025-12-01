from typing import TypedDict, List, Optional
from langgraph.graph import StateGraph, END


# ✅ Strong Typed State
class AgentState(TypedDict, total=False):
    metric: str
    months: List[int]
    query: str
    result: int
    response: str


def nlp_node(state: AgentState) -> AgentState:
    print("🧠 Understanding Query...")
    return {
        "metric": "GMV",
        "months": [11]   # already numeric to simplify demo
    }


def normalize_node(state: AgentState) -> AgentState:
    print("🔍 Normalizing data...")
    # Already numeric → pass through
    return state


def sql_node(state: AgentState) -> AgentState:
    print("🛠 Building SQL...")
    month = state["months"][0]
    query = f"SELECT SUM(order_value) FROM XYZ WHERE MONTH(order_date) = {month}"
    return {
        **state,
        "query": query
    }


def db_node(state: AgentState) -> AgentState:
    print("🗄 Simulating DB call...")
    return {
        **state,
        "result": 31000
    }


def format_node(state: AgentState) -> AgentState:
    print("📊 Formatting result...")
    response = f"Total GMV is ₹{state['result']}"
    print("✅ FINAL:", response)
    return {
        **state,
        "response": response
    }


# ✅ Build Graph
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

graph.invoke({})
