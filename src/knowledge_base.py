import json


class KnowledgeBase:

    def __init__(self, knowledge_base_path):
        try:
            with open(knowledge_base_path, "r") as f:
                self.knowledge_base = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"The specified JSON file '{knowledge_base_path}' was not found.")
        except json.JSONDecodeError:
            raise ValueError(f"The specified JSON file '{knowledge_base_path}' contains invalid JSON data.")

    def get_knowledge_base(self):
        return self.knowledge_base
