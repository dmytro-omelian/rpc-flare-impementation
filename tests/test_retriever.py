from src.retriever import Retriever


def test_retriever():
    knowledge_base_path = "data/knowledge_base.json"
    retriever = Retriever(knowledge_base_path)

    documents = retriever.retrieve_documents("The quick brown fox jumps over the lazy dog.")

    print(documents)


if __name__ == "__main__":

    test_retriever()