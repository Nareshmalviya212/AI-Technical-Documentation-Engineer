from src.embeddings import EmbeddingModel
from src.vector_store import FAISSVectorStore

class Retriever:

    def __init__(
        self,
        vector_store,
        embedding_model,
        top_k=3,
        score_threshold=0.60
    ):
        self.vector_store = vector_store
        self.embedding_model = embedding_model
        self.top_k = top_k
        self.score_threshold = score_threshold

    def retrieve(self, query):

        query_embedding = self.embedding_model.embed_query(
            query
        )

        results = self.vector_store.search(
            query_embedding,
            top_k=self.top_k
        )

        # Keep only sufficiently relevant results
        filtered_results = [
            result
            for result in results
            if result["score"] >= self.score_threshold
        ]

        return filtered_results