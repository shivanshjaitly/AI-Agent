# from orchestration.workflow import Workflow

# wf = Workflow()

# while True:
#     q = input("Ask Finance Bot > ")
#     if q.lower() == "exit":
#         break
#     response = wf.process(q)
#     print(response)
from src.finance_langgraph import graph

def main():
    print("\n💼 Finance AI Agent (Phase-2)")
    print("Type 'exit' to quit.\n")

    while True:
        q = input("Ask Finance Bot > ")

        if q.lower() in ["exit", "quit"]:
            print("👋 Bye!")
            break

        try:
            graph.invoke({"question": q})
        except Exception as e:
            print("❌ Error:", str(e))


if __name__ == "__main__":
    main()
