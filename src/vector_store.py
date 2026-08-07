import pickle
from pathlib import Path

import faiss
import numpy as np


class FAISSVectorStore:

    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)
        self.documents = []

    def add_documents(self, documents, embeddings):
        vectors = np.array(embeddings, dtype="float32")

        self.index.add(vectors)
        self.documents.extend(documents)

    def search(self, query_embedding, top_k=3):

        query_vector = np.array(
            [query_embedding],
            dtype="float32"
        )

        scores, indices = self.index.search(
            query_vector,
            top_k
        )

        results = []

        for score, index in zip(scores[0], indices[0]):

            if index == -1:
                continue

            results.append(
                {
                    "document": self.documents[index],
                    "score": float(score)
                }
            )

        return results

    def save(self, path="vector_store"):

        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)

        faiss.write_index(
            self.index,
            str(path / "index.faiss")
        )

        with open(path / "documents.pkl", "wb") as f:
            pickle.dump(self.documents, f)

    @classmethod
    def load(cls, path="vector_store"):

        path = Path(path)

        index = faiss.read_index(
            str(path / "index.faiss")
        )

        with open(path / "documents.pkl", "rb") as f:
            documents = pickle.load(f)

        store = cls(index.d)
        store.index = index
        store.documents = documents

        return store