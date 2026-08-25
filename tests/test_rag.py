from langchain_core.documents import Document

from src.rag_pipeline import RAGPipeline


class FakeRetriever:

    def retrieve(self, question):
        return [
            {
                "document": Document(
                    page_content="FastAPI is a Python web framework.",
                    metadata={
                        "source_name": "FastAPI Official Documentation",
                        "source_url": "https://fastapi.tiangolo.com/",
                        "category": "basics",
                        "topic": "introduction",
                        "filename": "fastapi_intro.md"
                    }
                ),
                "score": 0.90
            }
        ]


def test_rag_pipeline(monkeypatch):

    rag = RAGPipeline.__new__(RAGPipeline)

    rag.retriever = FakeRetriever()

    def fake_generate_response(prompt):
        assert "FastAPI is a Python web framework." in prompt
        return "FastAPI is a Python web framework."

    monkeypatch.setattr(
        "src.rag_pipeline.generate_response",
        fake_generate_response
    )

    result = rag.ask("What is FastAPI?")

    assert result["answer"] == (
        "FastAPI is a Python web framework."
    )

    assert len(result["sources"]) == 1

    assert (
        result["sources"][0]["filename"]
        == "fastapi_intro.md"
    )

    assert (
        result["sources"][0]["score"]
        == 0.90
    )