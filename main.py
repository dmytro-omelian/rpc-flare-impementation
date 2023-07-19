from src.flare import FLARE
from src.retriever import Retriever


def test_flare():
    print('test_flare')
    return 'test_flare'


if __name__ == '__main__':

    input = input('Enter a prompt: ')
    numbers_of_sentences = input('Enter the number of sentences to generate: ')

    knowledge_base_path = "data/knowledge_base.json"
    retriever = Retriever(knowledge_base_path)

    flare_model = FLARE("http://localhost:5000")

    next_sentence = flare_model.generate_text(prompt=input)
    while numbers_of_sentences > 0:

        next_sentence = flare_model.generate_text(prompt=next_sentence)
        numbers_of_sentences -= 1

