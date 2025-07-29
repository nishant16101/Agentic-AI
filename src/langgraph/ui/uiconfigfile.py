from configparser import ConfigParser

class Config:
    def __init__(self, config_file=".src/langgraph/ui/uiconfigfile.ini"):
        self.config_file = ConfigParser()
        self.config_file.read(config_file)

    def get_llm_options(self):
        value = self.config_file['DEFAULT'].get('LLM_OPTIONS', '')
        return value.split(",") if value else []

    def get_usecase_options(self):
        value = self.config_file['DEFAULT'].get('USECASE_OPTIONS', '')
        return value.split(",") if value else []

    def get_openai_models(self):
        value = self.config_file['DEFAULT'].get('OPENAI_MODELS', '')
        return [model.strip() for model in value.split(",")] if value else []

    def get_page_title(self):
        return self.config_file['DEFAULT'].get('PAGE_TITLE', 'LangGraph App')
