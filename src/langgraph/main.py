import streamlit as st
import os
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_ui():
    """Function to load the LangGraph UI using Streamlit."""
    ui = LoadStreamlitUI()
    user_input_ai = ui.load_streamlit_ui()
    if not user_input_ai:
        st.error("Failed to load user input. Please check your configuration.")
        return
    user_message = st.chat_input("Enter your message:")