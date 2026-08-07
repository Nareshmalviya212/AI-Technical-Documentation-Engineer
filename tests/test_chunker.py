from src.loader import DocumentLoader
from src.chunker import DocumentChunker


# Load documents
loader = DocumentLoader("data/documents")
documents = loader.load_documents()

print(f"Documents loaded: {len(documents)}")


# Create chunks
chunker = DocumentChunker(
    chunk_size=500,
    chunk_overlap=100
)

chunks = chunker.split_documents(documents)

print(f"Chunks created: {len(chunks)}")


# Display chunks
for i, chunk in enumerate(chunks, start=1):

    print("\n" + "=" * 60)
    print(f"CHUNK {i}")

    print("\nMetadata:")
    print(chunk.metadata)

    print("\nContent:")
    print(chunk.page_content)