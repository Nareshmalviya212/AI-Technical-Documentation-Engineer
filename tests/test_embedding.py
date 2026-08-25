from langchain_core.documents import Document

from src.embeddings import EmbeddingModel


class FakeEmbedding:

    def embed_documents(self, texts):
        return [
            [1.0, 0.0, 0.0]
            for _ in texts
        ]

    def embed_query(self, query):
        return [1.0, 0.0, 0.0]


def test_embed_documents(monkeypatch):

    embedding_model = EmbeddingModel.__new__(EmbeddingModel)

    embedding_model.model = FakeEmbedding()

    documents = [
        Document(page_content="FastAPI is a web framework."),
        Document(page_content="FastAPI supports dependencies.")
    ]

    vectors = embedding_model.embed_documents(documents)

    assert len(vectors) == 2
    assert len(vectors[0]) == 3


def test_embed_query(monkeypatch):

    embedding_model = EmbeddingModel.__new__(EmbeddingModel)

    embedding_model.model = FakeEmbedding()

    vector = embedding_model.embed_query(
        "What is FastAPI?"
    )

    assert len(vector) == 3