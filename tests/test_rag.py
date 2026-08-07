from src.rag_pipeline import RAGPipeline


rag = RAGPipeline(
    vector_store_path="vector_store",
    top_k=3
)


#question = "What is FastAPI and what can it be used for?"
question = "what is the capital of france?"


result = rag.ask(question)


print("\n" + "=" * 70)
print("QUESTION")
print("=" * 70)

print(question)


print("\n" + "=" * 70)
print("ANSWER")
print("=" * 70)

print(result["answer"])


print("\n" + "=" * 70)
print("SOURCES")
print("=" * 70)

for i, source in enumerate(
    result["sources"],
    start=1
):

    print(f"\nSource {i}")
    print("-" * 50)

    print("Source:", source["source_name"])
    print("Topic:", source["topic"])
    print("Document:", source["filename"])
    print("URL:", source["source_url"])
    print("Similarity:", source["score"])