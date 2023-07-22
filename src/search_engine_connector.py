from src.bm25 import BM25


class SearchEngineConnector:

    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.bm25 = BM25()

    def retrieve_documents(self, query, top_n=5):
        documents = [document["text"] for document in self.knowledge_base]
        top_docs = self.bm25.search(query, documents, top_n=top_n)
        return top_docs
