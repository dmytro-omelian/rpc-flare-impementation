from src.bm25 import BM25
from src.knowledge_base import KnowledgeBase


class SearchEngineConnector:

    def __init__(self, knowledge_base: KnowledgeBase):
        self.knowledge_base = knowledge_base

    def retrieve_documents(self, query: str, top_n=1):
        documents = [document["text"] for document in self.knowledge_base.get_knowledge_base()]
        self.bm25 = BM25(documents)

        top_docs = self.bm25.rank_documents(query, top_n=top_n)
        return top_docs
