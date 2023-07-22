import json


class KnowledgeBase:

    def __init__(self, knowledge_base_path):
        with open(knowledge_base_path, "r") as f:
            self.knowledge_base = json.load(f)

    def get_knowledge_base(self):
        return self.knowledge_base
