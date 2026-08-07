from src.embeddings import EmbeddingModel
from src.vector_store import FAISSVectorStore
from src.retriever import Retriever
from src.llm import generate_response
from src.prompt import build_prompt


class RAGPipeline:

    def __init__(
        self,
        vector_store_path="vector_store",
        top_k=3
    ):

        # Load embedding model
        self.embedding_model = EmbeddingModel()

        # Load FAISS vector store
        self.vector_store = FAISSVectorStore.load(
            vector_store_path
        )

        # Create retriever
        self.retriever = Retriever(
            vector_store=self.vector_store,
            embedding_model=self.embedding_model,
            top_k=top_k
        )

    def ask(self, question):

        # Retrieve relevant documents
        results = self.retriever.retrieve(question)

        # No relevant documentation found
        if not results:

            return {
                "answer": (
                    "I could not find this information "
                    "in the available technical documentation."
                ),
                "sources": []
            }

        # Build context
        context_parts = []

        for result in results:
            document = result["document"]

            context_parts.append(
                document.page_content
            )

        context = "\n\n---\n\n".join(context_parts)

        # Build prompt
        prompt = build_prompt(
            context=context,
            question=question
        )

        # Generate answer
        answer = generate_response(prompt)

        # ... keep the rest of your existing source-processing code

        # Prepare source information
        sources = []

        seen_sources = set()

        for result in results:

            document = result["document"]
            metadata = document.metadata

            source_key = metadata["filename"]

            # Avoid showing duplicate documents
            if source_key in seen_sources:
                continue

            seen_sources.add(source_key)

            sources.append({
                "source_name": metadata["source_name"],
                "source_url": metadata["source_url"],
                "category": metadata["category"],
                "topic": metadata["topic"],
                "filename": metadata["filename"],
                "score": result["score"]
            })

        return {
            "answer": answer,
            "sources": sources
        }