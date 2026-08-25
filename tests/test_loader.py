from src.loader import DocumentLoader


def test_load_documents():
    loader = DocumentLoader("data/documents")
    documents = loader.load_documents()

    assert len(documents) > 0

    for document in documents:
        assert document.page_content
        assert document.metadata["source_name"]
        assert document.metadata["source_url"]
        assert document.metadata["category"]
        assert document.metadata["topic"]
        assert document.metadata["filename"]