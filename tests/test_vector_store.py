from langchain_core.documents import Document

from src.vector_store import FAISSVectorStore


def test_add_and_search_documents():
    documents = [
        Document(page_content="FastAPI is a web framework."),
        Document(page_content="FastAPI supports dependency injection."),
        Document(page_content="Python is a programming language."),
    ]

    embeddings = [
        [1.0, 0.0, 0.0],
        [0.9, 0.1, 0.0],
        [0.0, 0.0, 1.0],
    ]

    vector_store = FAISSVectorStore(dimension=3)

    vector_store.add_documents(
        documents,
        embeddings
    )

    results = vector_store.search(
        [1.0, 0.0, 0.0],
        top_k=2
    )

    assert len(results) == 2
    assert results[0]["document"].page_content == "FastAPI is a web framework."
    assert results[0]["score"] > results[1]["score"]


def test_save_and_load_vector_store(tmp_path):
    documents = [
        Document(page_content="FastAPI is a web framework.")
    ]

    embeddings = [
        [1.0, 0.0, 0.0]
    ]

    vector_store = FAISSVectorStore(dimension=3)

    vector_store.add_documents(
        documents,
        embeddings
    )

    save_path = tmp_path / "vector_store"

    vector_store.save(save_path)

    loaded_store = FAISSVectorStore.load(save_path)

    results = loaded_store.search(
        [1.0, 0.0, 0.0],
        top_k=1
    )

    assert len(results) == 1
    assert results[0]["document"].page_content == (
        "FastAPI is a web framework."
    )