from src import llm


class FakeMessage:
    content = "FastAPI is a modern Python web framework."


class FakeChoice:
    message = FakeMessage()


class FakeResponse:
    choices = [FakeChoice()]


class FakeCompletions:

    def create(self, **kwargs):
        return FakeResponse()


class FakeChat:
    completions = FakeCompletions()


class FakeClient:
    chat = FakeChat()


def test_generate_response(monkeypatch):

    monkeypatch.setattr(
        llm,
        "Groq",
        lambda api_key: FakeClient()
    )

    monkeypatch.setenv(
        "GROQ_API_KEY",
        "fake-test-key"
    )

    answer = llm.generate_response(
        "What is FastAPI?"
    )

    assert answer == (
        "FastAPI is a modern Python web framework."
    )