class RetrievalService:

    def __init__(self, language_model):
        self.language_model = language_model


    def retrieve(self, possible_next_sentence):
        count_low_probability_tokens = 0
        for token_and_prob in possible_next_sentence:
            token, prob = token_and_prob
            if prob < 0.1:
                count_low_probability_tokens += 1
        if count_low_probability_tokens > 0:
            return self.retrieve_low_probability_tokens(possible_next_sentence)
        return possible_next_sentence[0][0]

    def retrieve_low_probability_tokens(self, tokens_and_probs, threshold=0.1):
        low_probability_tokens = []
        for token_and_prob in tokens_and_probs:
            token, prob = token_and_prob
            if prob < threshold:
                low_probability_tokens.append(token)
        return low_probability_tokens