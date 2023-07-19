import random
import json
import requests

class FLARE:

    def __init__(self, knowledge_base_url):
        self.knowledge_base_url = knowledge_base_url

    def generate_text(self, prompt):
        prediction = self.predict_next_sentence(prompt)
        documents = self.retrieve_documents(prediction)
        next_sentence = self.generate_sentence(documents)
        return next_sentence

    def predict_next_sentence(self, prompt):
        probabilities = requests.get(f"{self.knowledge_base_url}/predict_next_sentence?prompt={prompt}").json()
        prediction = random.choice(list(probabilities.keys()))
        return prediction

    def retrieve_documents(self, prediction):
        documents = requests.get(f"{self.knowledge_base_url}/retrieve_documents?prediction={prediction}").json()
        return documents

    def generate_sentence(self, documents):
        words = []
        for document in documents:
            words += document.split()
        return " ".join(words)
