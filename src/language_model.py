import json

from src.search_engine_connector import SearchEngineConnector


class LanguageModel:

    def __init__(self):
        self.sentences = json.load(open("data/joe-biden.json", "r"))
        self.current_sentence = 0

    def predict_next_sentence(self, input, previous_sentences):
        search_engine_connector = SearchEngineConnector("data/knowledge_base.json")

        retrieve_documents_query = self.construct_retrieval_document_prompt(input, previous_sentences)
        top_docs = search_engine_connector.retrieve_documents(retrieve_documents_query, top_n=5)
        top_docs = [document["text"] for document in top_docs]

        query = self.construct_doc_formatting_prompt(top_docs, input)

        next_sentence = self.fetch_next_sentence(query)
        return next_sentence

    def fetch_next_sentence(self, prompt):
        current_sentence = self.sentences[f'sentence_{self.current_sentence}-tokens-and-probs'][self.current_sentence]
        self.current_sentence += 1
        return current_sentence

    def construct_doc_formatting_prompt(self, DOCUMENTS, x):
        prompt = "Documents: "
        for document in DOCUMENTS:
            prompt += f'[{document["id"]}]: {document["text"]}'
        prompt += f'The user input is: {x}'
        return prompt

    def construct_zero_shot_question_generation_prompt(self, x, y_t, z):
        prompt = f"""
        The user input is: {x}
        Generated output so far: {y_t}
        
        Given the above passage, ask a question to which the answer is "{z}".
        """
        return prompt

    def construct_retrieval_document_prompt(self, input, previous_sentences):
        prompt = f"""
            The user input is: {input}\n"
            The generated output so far is: {previous_sentences}\n"
            Given the above passage, retrieve the most relevant documents from the knowledge base.
        """
        return prompt
