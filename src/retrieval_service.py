from src.language_model import LanguageModel


class RetrievalService:

    def __init__(self, language_model: LanguageModel):
        self.language_model = language_model


    def retrieve(self, possible_next_sentence):
        return possible_next_sentence

    def retrieve_low_probability_tokens(self, tokens_and_probs, threshold=0.1):
        low_probability_tokens = []
        for token_and_prob in tokens_and_probs:
            token, prob = token_and_prob
            if prob < threshold:
                low_probability_tokens.append(token)
        return low_probability_tokens