import random
import json


class FLARE:

    def __init__(self, knowledge_base_path):
        with open(knowledge_base_path, "r") as f:
            self.knowledge_base = json.load(f)

    def generate_text(self, prompt):
        prediction = self.predict_next_sentence(prompt)
        documents = self.knowledge_base.get_documents(prediction)
        next_sentence = self.generate_sentence(documents)
        return next_sentence

    def predict_next_sentence(self, prompt):
        probabilities = self.language_model.predict_next_sentence(prompt)
        prediction = random.choice(list(probabilities.keys()))
        return prediction

    def generate_sentence(self, documents):
        words = []
        for document in documents:
            words += document.split()
        return " ".join(words)

