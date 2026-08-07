from src.loader import DocumentLoader

loader = DocumentLoader("data/documents")

docs = loader.load_documents()

print(f"\nLoaded {len(docs)} document(s)\n")

for i, doc in enumerate(docs, start=1):
    print(f"\nDocument {i}")
    print("-" * 50)
    print("Metadata:", doc.metadata)
    print("\nContent:")
    print(doc.page_content)