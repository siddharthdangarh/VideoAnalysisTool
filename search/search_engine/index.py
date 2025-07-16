import faiss
import logging
import numpy as np
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)


class VideoSearchEngine:
    def __init__(self, chunks: list):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = self._build_index(chunks)

    def _build_index(self, chunks: list):
        texts = [chunk["text"] for chunk in chunks]
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        self.embeddings = embeddings  # store for lookup
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings)
        return index

    def search(self, query: str, top_k: int = 1):
        try:
            query_embedding = self.model.encode([query], convert_to_numpy=True)
            D, I = self.index.search(query_embedding, top_k)
            results = [self.chunks[i] for i in I[0]]
            return results
        except Exception as e:
            logger.exception(e)
            return None
