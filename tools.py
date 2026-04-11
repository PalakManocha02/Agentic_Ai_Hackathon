from crewai.tools import tool
import requests
import os
from tavily import TavilyClient

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# Web search — you WILL need this
@tool("Web Search")
def web_search(query: str) -> str:
    """Search the web for current information."""
    results = tavily.search(query=query, max_results=5)
    return str(results)

# File reader — useful for reading JDs, resumes etc
@tool("Read File")
def read_file(filepath: str) -> str:
    """Read contents of a file."""
    with open(filepath, "r") as f:
        return f.read()

# Write file — useful for saving outputs
@tool("Write File")
def write_file(filepath: str, content: str) -> str:
    """Write content to a file."""
    with open(filepath, "w") as f:
        f.write(content)
    return f"Written to {filepath}"

# Generic API caller — useful if problem involves hitting an API
@tool("Call API")
def call_api(url: str, method: str = "GET", payload: str = "") -> str:
    """Make an HTTP request to an API endpoint."""
    if method == "GET":
        response = requests.get(url)
    else:
        response = requests.post(url, json=eval(payload))
    return response.text