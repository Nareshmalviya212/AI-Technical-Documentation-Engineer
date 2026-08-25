from src.loader import DocumentLoader
from src.chunker import DocumentChunker


def test_split_documents_into_chunks():
    loader = DocumentLoader("data/documents")
    documents = loader.load_documents()

    chunker = DocumentChunker(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = chunker.split_documents(documents)

    assert len(chunks) > 0

    for chunk in chunks:
        assert chunk.page_content
        assert "chunk_id" in chunk.metadata