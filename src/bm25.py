import numpy as np
from beir.retrieval.search.lexical import BM25Search
from nltk.tokenize.punkt import PunktSentenceTokenizer


class BM25:

    def __init__(self):
        pass

    def search(self, query, documents, top_n=5):
        tokenizer = PunktSentenceTokenizer()
        query_tokens = tokenizer.tokenize(query)
        documents_tokens = [tokenizer.tokenize(document) for document in documents]

        bm25 = BM25Search(documents_tokens)
        doc_scores = bm25.get_scores(query_tokens)
        doc_indices_sorted = np.argsort(doc_scores)[::-1]
        top_docs = [documents[idx] for idx in doc_indices_sorted[:top_n]]
        return top_docs
