import faiss
import pickle
from typing import List
import os

from embedding import load_index

class RetrieverTool:
    def __init__(self, store_dir="store"):
        self.index, self.texts = load_index(store_dir)

    def run(self, query: str) -> str:
        """Searches the index for the query and returns the most relevant text chunk."""
        query_embedding = self._embed_query(query)
        D, I = self.index.search(query_embedding, k=3)  # Top 3 results
        results = [self.texts[i] for i in I[0] if i != -1]
        return "\n\n".join(results)

    def _embed_query(self, query: str):

        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("all-MiniLM-L6-v2")
        return model.encode([query])

def retrieve_function(query: str) -> str:
    """Function wrapper with type hints for pydantic-ai."""
    global _retriever_instance
    if '_retriever_instance' not in globals():
        _retriever_instance = RetrieverTool()
    return _retriever_instance.run(query)
