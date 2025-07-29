from configparser import ConfigParser
import os

class Config:
    def __init__(self, config_file="src/langgraph/ui/uiconfigfile.ini"):
        self.config_file = ConfigParser()
        
        # Try multiple possible paths
        possible_paths = [
            config_file,
            "src/langgraph/ui/uiconfigfile.ini",
            "./src/langgraph/ui/uiconfigfile.ini",
            "uiconfigfile.ini",
            "src/ui/uiconfigfile.ini"
        ]
        
        config_found = False
        for path in possible_paths:
            if os.path.exists(path):
                print(f"Found config file at: {path}")
                self.config_file.read(path)
                config_found = True
                break
        
        if not config_found:
            print(f"Config file not found. Tried paths: {possible_paths}")
            print(f"Current working directory: {os.getcwd()}")
            print(f"Files in current directory: {os.listdir('.')}")
            # Create default config in memory
            self.config_file.read_string("""
[DEFAULT]
PAGE_TITLE = LANGGRAPH : BUILDING AI APPLICATIONS WITH LANGCHAIN AND LANGGRAPH
LLM_OPTIONS = openai
USECASE_OPTIONS = Basic Chatbot
OPENAI_MODELS = gpt-3.5-turbo, gpt-4, gpt-4-1106-preview, gpt-4-vision-preview
            """)

    def get_llm_options(self):
        value = self.config_file['DEFAULT'].get('LLM_OPTIONS', '')
        return [option.strip() for option in value.split(",")] if value else []

    def get_usecase_options(self):
        value = self.config_file['DEFAULT'].get('USECASE_OPTIONS', '')
        return [option.strip() for option in value.split(",")] if value else []

    def get_openai_models(self):
        value = self.config_file['DEFAULT'].get('OPENAI_MODELS', '')
        return [model.strip() for model in value.split(",")] if value else []

    def get_page_title(self):
        return self.config_file['DEFAULT'].get('PAGE_TITLE', 'LangGraph App')