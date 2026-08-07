from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:

    def __init__(self):
        self.model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5",
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )

    def embed_documents(self, documents):
        texts = [doc.page_content for doc in documents]

        return self.model.embed_documents(texts)

    def embed_query(self, query):
        return self.model.embed_query(query)