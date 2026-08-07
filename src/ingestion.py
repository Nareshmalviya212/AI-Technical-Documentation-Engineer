from src.loader import DocumentLoader
from src.chunker import DocumentChunker
from src.embeddings import EmbeddingModel
from src.vector_store import FAISSVectorStore


DATA_PATH = "data/documents"
VECTOR_STORE_PATH = "vector_store"


def build_vector_store():

    print("\n" + "=" * 60)
    print("STARTING DOCUMENT INGESTION")
    print("=" * 60)

    # -----------------------------------
    # 1. Load documents
    # -----------------------------------

    print("\n[1/5] Loading documents...")

    loader = DocumentLoader(DATA_PATH)
    documents = loader.load_documents()

    print(f"Loaded documents: {len(documents)}")

    if not documents:
        raise ValueError(
            "No documents found in data/documents/"
        )

    # -----------------------------------
    # 2. Chunk documents
    # -----------------------------------

    print("\n[2/5] Creating chunks...")

    chunker = DocumentChunker(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = chunker.split_documents(documents)

    print(f"Created chunks: {len(chunks)}")

    # -----------------------------------
    # 3. Generate embeddings
    # -----------------------------------

    print("\n[3/5] Generating embeddings...")

    embedding_model = EmbeddingModel()

    embeddings = embedding_model.embed_documents(
        chunks
    )

    print(f"Generated embeddings: {len(embeddings)}")

    # -----------------------------------
    # 4. Create FAISS vector store
    # -----------------------------------

    print("\n[4/5] Building FAISS vector store...")

    dimension = len(embeddings[0])

    vector_store = FAISSVectorStore(
        dimension=dimension
    )

    vector_store.add_documents(
        chunks,
        embeddings
    )

    print(
        f"FAISS vectors: "
        f"{vector_store.index.ntotal}"
    )

    # -----------------------------------
    # 5. Save vector store
    # -----------------------------------

    print("\n[5/5] Saving vector store...")

    vector_store.save(
        VECTOR_STORE_PATH
    )

    print(
        f"Vector store saved to: "
        f"{VECTOR_STORE_PATH}/"
    )

    print("\n" + "=" * 60)
    print("INGESTION COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    build_vector_store()