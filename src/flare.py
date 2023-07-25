from src.knowledge_base import KnowledgeBase
from src.language_model import LanguageModel


class FLARE:
    def __init__(self, language_model: LanguageModel, knowledge_base: KnowledgeBase):
        self.language_model = language_model
        self.knowledge_base = knowledge_base

    def predict_next_sentence(self, prompt: str, previous_sentences: [str]):
        prediction = self.language_model.predict_next_sentence(prompt, previous_sentences)
        return prediction
