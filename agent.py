# agent.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub

from tools import web_search, calculator

# Load API key from .env file
load_dotenv()

# Set up the AI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Tools the agent can use
tools = [web_search, calculator]

# Pull ReAct prompt from LangChain Hub
prompt = hub.pull("hwchase17/react")

# Create the agent
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# Wrap in executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=8,
    handle_parsing_errors=True
)