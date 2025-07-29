import os
import streamlit as st
from langchain_openai import ChatOpenAI

class OpenAILLM:
    def __init__(self,user_controls_input):
        self.user_controls = user_controls_input
    
    def get_llm_mode(self):
        try:
            openai_api_key = self.user_controls['openai_api_key']
            selected_model = self.user_controls['selected_model']
            if openai_api_key == '' and os.environ['openai_api_key'] =='':
                st.error("Please Enter Open AI key")
            llm = ChatOpenAI(api_key=openai_api_key,model=selected_model)
        except Exception as e:
            raise ValueError(f'error occured with exception:{e}')
        return llm

        