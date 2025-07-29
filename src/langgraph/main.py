import streamlit as st
import os
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph.LLMS.openai_llm import OpenAILLM
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.ui.streamlitui.display_result import DisplayResultsStreamlit

def load_langgraph_ui():
    """Function to load the LangGraph UI using Streamlit."""
    ui = LoadStreamlitUI()
    user_input_ai = ui.load_streamlit_ui()
    
    if not user_input_ai:
        st.error("Failed to load user input. Please check your configuration.")
        return
    
    user_message = st.chat_input("Enter your message:")
    
    if user_message:
        try:
            # Initialize LLM
            obj_llm_config = OpenAILLM(user_controls_input=user_input_ai)
            model = obj_llm_config.get_llm_mode()
            
            if not model:
                st.error("Error: LLM model could not be initialized")
                return
            
            # Get use case
            usecase = user_input_ai.get('selected_usecase')
            if not usecase:
                st.error("Error: No use case selected")
                return
            
            # Initialize graph builder
            graph_builder = GraphBuilder(model)
            
            try:
                # Setup graph and get the compiled graph
                graph_builder.setup_graph(usecase)
                compiled_graph = graph_builder.graph_builder.compile()
                
                # Display results with the compiled graph and user message
                display_handler = DisplayResultsStreamlit(usecase, compiled_graph, user_message)
                display_handler.display_result_on_ui()
                
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return
                
        except Exception as e:
            st.error(f"Error occurred: {e}")
            return