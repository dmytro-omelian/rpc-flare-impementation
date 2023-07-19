import json

class Retriever:

    def __init__(self, knowledge_base_path):
        with open(knowledge_base_path, "r") as f:
            self.knowledge_base = json.load(f)

    def retrieve_documents(self, prediction):
        documents = []
        for document in self.knowledge_base:
            if prediction in document["sentences"]:
                documents.append(document)
        return documents
