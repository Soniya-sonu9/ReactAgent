# ReactAgent
AI Agent using ReAct pattern with LangChain

# 🤖 ReAct AI Agent (Reason + Act)

## 📌 Project Overview

This project is an **AI Agent built using LangChain** that can perform
multi-step reasoning and take actions using external tools to solve complex queries.

Unlike traditional chatbots, this agent:
- 🧠 Thinks step by step
- 🔍 Decides what action to take
- ⚙️ Uses tools like web search and calculator
- ✅ Combines results for accurate final answers

---

## 🧠 Core Concept — ReAct Pattern

The agent follows the **ReAct Pattern (Reason + Act)**
User Query
↓
Thought  → Agent decides what to do
↓
Action   → Agent calls a tool
↓
Observation → Agent reads the result
↓
Repeat until confident
↓
Final Answer

---

## 🗂️ Project Structure
ReactAgent/
├── agent.py          # Agent brain and ReAct loop
├── tools.py          # Web search and calculator tools
├── main.py           # Run the agent
├── .env.example      # Example environment variables
└── requirements.txt  # All dependencies

---

## ⚙️ Tech Stack

- Python 3.11
- LangChain
- OpenAI API (GPT-4o-mini)
- DuckDuckGo Search API

---

## 🚀 Features

- Multi-step reasoning using ReAct loop
- Web search tool for current information
- Calculator tool for math expressions
- Modular and easy to extend

---

## 🛠️ Setup and Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/react-agent.git
cd react-agent
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key
```bash
OPENAI_API_KEY=your-openai-key-here
```

---

## ▶️ Run the Agent
```bash
python main.py
```

---

## 📊 Example Output

❓ Question: What is population of India? Calculate 1% of it.
Thought: I need to search for India's population
Action: web_search
Observation: India's population is 1.44 billion
Thought: Now calculate 1%
Action: calculator
Observation: 14,400,000
Final Answer: 1% of India's population is 14.4 million

---

## 💬 Interview Line

> This is a ReAct-based AI agent that performs multi-step reasoning
> and dynamically uses tools like web search and calculator
> to solve complex queries accurately.

---

⭐ Star this repo if you found it helpful!
