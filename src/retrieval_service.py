from src.language_model import LanguageModel


class RetrievalService:

    def __init__(self, language_model: LanguageModel):
        self.language_model = language_model

    def retrieve(self, possible_next_sentence: str, user_input: str, generated_sentences: [str]):
        low_probability_tokens = self.retrieve_low_probability_tokens(possible_next_sentence)
        replacement_tokens = self.language_model.get_replacement_tokens(
            low_probability_tokens,
            user_input,
            generated_sentences
        )
        possible_next_sentence = self.replace_tokens(possible_next_sentence, replacement_tokens)

        return possible_next_sentence


    def replace_tokens(self, possible_next_sentence: [[str]], replacement_tokens: [[str]], threshold=0.2):
        result = []
        index = 0
        temp = []
        replacement_tokens = [token for tokens in replacement_tokens for token in tokens]
        for token_and_prob in possible_next_sentence:
            token, prob = token_and_prob
            if prob > threshold:
                if len(temp) > 0:
                    for i in range(len(temp)):
                        result.append(replacement_tokens[index])
                        index += 1
                    temp = []
                result.append(token_and_prob)
            else:
                temp.append(token)
        if len(temp) > 0:
            result.append(replacement_tokens[index])
        return result

    def retrieve_low_probability_tokens(self, tokens_and_probs, threshold=0.2):
        low_probability_tokens = []
        temp = []
        for token_and_prob in tokens_and_probs:
            token, prob = token_and_prob
            if prob < threshold:
                temp.append(token_and_prob)
            else:
                if len(temp) > 0:
                    low_probability_tokens.append(temp)
                    temp = []
        if len(temp) > 0:
            low_probability_tokens.append(temp)
        return low_probability_tokens

    def is_retrieval_query(self, possible_next_sentence, threshold=0.2):
        for token_and_prob in possible_next_sentence:
            token, prob = token_and_prob
            if prob < threshold:
                return True
        return False
