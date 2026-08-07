from src.loader import DocumentLoader
from src.chunker import DocumentChunker
from src.embeddings import EmbeddingModel


# 1. Load documents
loader = DocumentLoader("data/documents")
documents = loader.load_documents()

print(f"Documents loaded: {len(documents)}")


# 2. Chunk documents
chunker = DocumentChunker(
    chunk_size=500,
    chunk_overlap=100
)

chunks = chunker.split_documents(documents)

print(f"Chunks created: {len(chunks)}")


# 3. Load embedding model
print("\nLoading embedding model...")

embedding_model = EmbeddingModel()

print("Embedding model loaded.")


# 4. Generate embeddings
vectors = embedding_model.embed_documents(chunks)

print(f"\nNumber of vectors: {len(vectors)}")

if vectors:
    print(f"Vector dimension: {len(vectors[0])}")

    print("\nFirst vector:")
    print(vectors[0][:10])