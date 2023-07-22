import random


class FLARE:
    def __init__(self, language_model, knowledge_base):
        self.language_model = language_model
        self.knowledge_base = knowledge_base

    def predict_next_sentence(self, prompt, previous_sentences):
        prediction = self.language_model.predict_next_sentence(prompt, previous_sentences)
        return prediction


