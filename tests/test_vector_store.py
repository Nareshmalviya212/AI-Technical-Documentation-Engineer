from src.loader import DocumentLoader
from src.chunker import DocumentChunker
from src.embeddings import EmbeddingModel
from src.vector_store import FAISSVectorStore


# -----------------------------
# 1. Load documents
# -----------------------------

loader = DocumentLoader("data/documents")

documents = loader.load_documents()

print(f"Documents loaded: {len(documents)}")


# -----------------------------
# 2. Chunk documents
# -----------------------------

chunker = DocumentChunker(
    chunk_size=500,
    chunk_overlap=100
)

chunks = chunker.split_documents(documents)

print(f"Chunks created: {len(chunks)}")


# -----------------------------
# 3. Create embeddings
# -----------------------------

embedding_model = EmbeddingModel()

embeddings = embedding_model.embed_documents(chunks)

print(f"Embeddings generated: {len(embeddings)}")


# -----------------------------
# 4. Create FAISS
# -----------------------------

dimension = len(embeddings[0])

vector_store = FAISSVectorStore(
    dimension=dimension
)

vector_store.add_documents(
    chunks,
    embeddings
)

print(f"FAISS vectors: {vector_store.index.ntotal}")


# -----------------------------
# 5. Test semantic search
# -----------------------------

query = "How can I build APIs using FastAPI?"

query_embedding = embedding_model.embed_query(query)

results = vector_store.search(
    query_embedding,
    top_k=3
)


# -----------------------------
# 6. Display results
# -----------------------------

print("\n" + "=" * 60)
print("SEARCH RESULTS")
print("=" * 60)

for i, result in enumerate(results, start=1):

    document = result["document"]
    score = result["score"]

    print(f"\nResult {i}")
    print("-" * 60)

    print("Similarity Score:", score)

    print("Metadata:")
    print(document.metadata)

    print("\nContent:")
    print(document.page_content)

# Save vector database

vector_store.save("vector_store")

print("\nVector store saved successfully.")