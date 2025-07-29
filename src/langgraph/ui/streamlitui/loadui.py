import streamlit as st
import os
from src.langgraph.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}
        
    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())
        
        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
            
            # Debug information
            st.write(f"Debug - LLM Options: {llm_options}")
            st.write(f"Debug - Use Case Options: {usecase_options}")
            
            # Check if options are loaded
            if not llm_options:
                st.error("No LLM options found. Please check your config file.")
                return None
                
            if not usecase_options:
                st.error("No use case options found. Please check your config file.")
                return None
            
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", llm_options)

            # Add null check before calling lower()
            if self.user_controls['selected_llm'] and self.user_controls['selected_llm'].lower() == 'openai':
                openai_models = self.config.get_openai_models()
                
                if not openai_models:
                    st.error("No OpenAI models found. Please check your config file.")
                    return None
                    
                self.user_controls['selected_model'] = st.selectbox("Select OpenAI Model", openai_models)
                self.user_controls['openai_api_key'] = st.text_input("OpenAI API Key", type="password")

                if not self.user_controls['openai_api_key']:
                    st.warning("Please enter your OpenAI API Key to proceed.")
            
            self.user_controls['selected_usecase'] = st.selectbox("Select Use Case", usecase_options)
        
        return self.user_controls