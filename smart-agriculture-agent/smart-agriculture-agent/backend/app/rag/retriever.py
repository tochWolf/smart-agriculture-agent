import re
from .knowledge_base import load_knowledge

class SimpleRetriever:
    def __init__(self):
        self.documents = [x.strip() for x in load_knowledge().split("\n\n") if x.strip()]

    def retrieve(self, query, top_k=3):
        query_words = set(re.findall(r"\w+", query.lower()))
        scored = []
        for document in self.documents:
            words = set(re.findall(r"\w+", document.lower()))
            scored.append((len(query_words & words), document))
        scored.sort(reverse=True, key=lambda x: x[0])
        return [doc for score, doc in scored[:top_k] if score > 0]

retriever = SimpleRetriever()
