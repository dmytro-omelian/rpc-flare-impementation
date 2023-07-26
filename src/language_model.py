import json

from src.search_engine_connector import SearchEngineConnector


class LanguageModel:

    def __init__(self, search_engine_connector: SearchEngineConnector):
        self.sentences = json.load(open("data/joe-biden.json", "r"))
        self.current_sentence = 1
        self.search_engine_connector = search_engine_connector

    def predict_next_sentence(self, input: str, previous_sentences: [str]):
        retrieve_documents_query = self.construct_retrieval_document_prompt(input, previous_sentences)
        top_docs = self.search_engine_connector.retrieve_documents(retrieve_documents_query)
        top_docs = [document for document, _ in top_docs]

        query = self.construct_doc_formatting_prompt(top_docs, input)

        next_sentence = self.fetch_next_sentence(query)
        return next_sentence

    def fetch_next_sentence(self, prompt: str):
        if self.current_sentence > 3:
            return None
        current_sentence = self.sentences[f'sentence{self.current_sentence}-tokens-and-probs']
        self.current_sentence += 1
        return current_sentence

    def construct_doc_formatting_prompt(self, DOCUMENTS: [str], x: str):
        prompt = "Documents: "
        for i, document in enumerate(DOCUMENTS):
            prompt += f'[{i}]: {document}\n'
        prompt += f'The user input is: {x}'
        return prompt

    def construct_retrieval_document_prompt(self, input: str, previous_sentences: [[str]]):
        previous_text = "".join([token for sentence in previous_sentences for token, prob in sentence])
        prompt = f"""
            The user input is: {input}\n"
            The generated output so far is: {previous_text}\n"
            Given the above passage, retrieve the most relevant documents from the knowledge base.
        """
        return prompt

    def get_replacement_tokens(self, low_probability_tokens, user_input, generated_sentences):
        result = []
        for tokens in low_probability_tokens:
            answer = " ".join([token for token, prob in tokens])

            prompt = self.construct_zero_shot_question_generation_prompt(user_input, generated_sentences, answer)
            question = self.get_question(prompt)
            replacement_tokens = self.get_answer(question, tokens)
            result.append(replacement_tokens)
        return result

    def construct_zero_shot_question_generation_prompt(self, x: str, y_t: str, z: str):
        prompt = f"""
        The user input is: {x}
        Generated output so far: {y_t}

        Given the above passage, ask a question to which the answer is "{z}".
        """
        return prompt

    def get_question(self, prompt):
        # TODO implement this with gpt api
        return "Question"

    def get_answer(self, prompt, tokens):
        # FIXME we don't need the tokens here (we use them to have a placeholder for the answer)

        correct_answers = json.load(open("data/correct_answers.json", "r"))

        for i, token in enumerate(tokens):
            value, prob = token
            replacement = self.contains_token(correct_answers, value)
            if replacement is not None:
                tokens[i] = replacement
            else:
                tokens[i] = [value, 0.5]


        return tokens

    def contains_token(self, correct_answers, token):
        for obj in correct_answers:
            if obj['wrong_token'] == token:
                return obj['correct_token']
        return None
