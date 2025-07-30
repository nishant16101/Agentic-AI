from langgraph.graph import StateGraph,START,END
from src.langgraph.state.state import State
from src.langgraph.nodes.chatbot import BasicChatbotNode
from src.langgraph.tools.tool import get_tools,create_tools
from langgraph.prebuilt import tools_condition,ToolNode
from src.langgraph.nodes.node import ChatbotWithToolNode
import os

class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using langgraph
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node('chatbot',self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_edge('chatbot',END)

    def chatbot_with_tools(self):
        # Get API key from environment
        tavily_api_key = os.getenv('TAVILY_API_KEY')
        if not tavily_api_key:
            raise ValueError("TAVILY_API_KEY not found in environment variables")
            
        tools = get_tools(tavily_api_key)
        tool_node = create_tools(tools)
        #define llm
        llm = self.llm

        obj_chatbot = ChatbotWithToolNode(llm)
        chatbot_node = obj_chatbot.create_chatbot(tools)

        #add node
        self.graph_builder.add_node('chatbot',chatbot_node)
        self.graph_builder.add_node('tools',tool_node)

        #define conditional and direct edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self,usecase:str):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "Chatbot with Web":
            self.chatbot_with_tools()
        
        return self.graph_builder.compile()