import warnings
import os
warnings.filterwarnings("ignore", category=DeprecationWarning)

try:
    # Try the new import first
    from langchain_tavily import TavilySearchResults
except ImportError:
    # Fallback to the old import if new package not available
    from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import ToolNode

def get_tools(tavily_api_key=None):
    # Use provided key or get from environment
    api_key = tavily_api_key or os.getenv('TAVILY_API_KEY')
    
    if not api_key:
        raise ValueError("TAVILY_API_KEY not found in environment variables or parameters")
    
    tools = [TavilySearchResults(max_results=2, tavily_api_key=api_key)]
    return tools

def create_tools(tools):
    return ToolNode(tools=tools)