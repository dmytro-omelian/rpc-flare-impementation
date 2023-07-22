from src.flare import FLARE
from src.language_model import LanguageModel
from src.retrieval_service import RetrievalService
from src.search_engine_connector import SearchEngineConnector
from src.knowledge_base import KnowledgeBase

def test_flare():
    print('test_flare')
    return 'test_flare'


if __name__ == '__main__':

    input = input('Enter a prompt: ')

    knowledge_base_path = "data/knowledge_base.json"
    knowledge_base = KnowledgeBase(knowledge_base_path)
    search_engine = SearchEngineConnector(knowledge_base_path)
    language_model = LanguageModel()


    retrieval_service = RetrievalService(language_model)
    flare_model = FLARE(language_model, knowledge_base)

    generated_sentences = []
    query_prompt = input
    while True:
        possible_next_sentence = flare_model.predict_next_sentence(query_prompt, generated_sentences)
        next_sentence = retrieval_service.retrieve(possible_next_sentence)
        generated_sentences.append(next_sentence)



