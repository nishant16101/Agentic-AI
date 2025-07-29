from typing_extensions import TypedDict, List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    Represent the structure of state used in graph
    """
    messages: Annotated[list, add_messages]  # Fixed: was 'message', should be 'messages'