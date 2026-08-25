from langchain_core.documents import Document

from src.retriever import Retriever


class FakeEmbeddingModel:

    def embed_query(self, query):
        return [1.0, 0.0, 0.0]


class FakeVectorStore:

    def search(self, query_embedding, top_k):
        return [
            {
                "document": Document(
                    page_content="Relevant FastAPI documentation."
                ),
                "score": 0.85
            },
            {
                "document": Document(
                    page_content="Less relevant documentation."
                ),
                "score": 0.40
            }
        ]


def test_retriever_filters_by_score():

    retriever = Retriever(
        vector_store=FakeVectorStore(),
        embedding_model=FakeEmbeddingModel(),
        top_k=3,
        score_threshold=0.60
    )

    results = retriever.retrieve("What is FastAPI?")

    assert len(results) == 1
    assert results[0]["score"] == 0.85
    assert (
        results[0]["document"].page_content
        == "Relevant FastAPI documentation."
    )