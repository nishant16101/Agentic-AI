from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    Represent the structure of state used in graph
    """
    message:Annotated[list,add_messages]