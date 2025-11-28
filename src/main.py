from orchestration.workflow import Workflow

wf = Workflow()

while True:
    q = input("Ask Finance Bot > ")
    if q.lower() == "exit":
        break
    response = wf.process(q)
    print(response)
