# tools.py
# Tools are like the agent's hands — it uses these to interact with the world

from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

# This tool lets the agent search the internet
search_tool = DuckDuckGoSearchRun()

@tool
def web_search(query: str) -> str:
    """Search the web for current information. Use this for any factual questions."""
    result = search_tool.run(query)
    return result

# This tool lets the agent do math calculations
@tool
def calculator(expression: str) -> str:
    """
    Calculate a math expression. 
    Example inputs: '25 * 4', '100 / 3', '2 ** 10'
    """
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Error in calculation: {e}"