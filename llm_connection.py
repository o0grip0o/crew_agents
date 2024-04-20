import os

from langchain.llms import Ollama

class LLMConnection():
    def __init__(self):
        self.model="crewai-mixtral:8x22b"
        self.base_url="http://localhost:11434/v1"

    def get_llm(self):
        return Ollama(
            model=self.model,
            base_url=self.base_url
        )