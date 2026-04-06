# main.py
# Run this file to start your agent!

from agent import agent_executor

print("🤖 ReAct AI Agent is ready!\n")

# You can change these questions to anything you want
questions = [
    "What is the current population of India? Then calculate 1% of that number.",
    "Who is the CEO of Tesla? Search and tell me.",
    "Calculate: 256 * 13 + 500"
]

for question in questions:
    print("\n" + "="*60)
    print(f"❓ Question: {question}")
    print("="*60)
    
    response = agent_executor.invoke({"input": question})
    
    print(f"\n✅ Final Answer: {response['output']}")