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


def test_generate_response(monkeypatch):

    monkeypatch.setattr(
        llm.client.chat,
        "completions",
        FakeCompletions()
    )

    answer = llm.generate_response(
        "What is FastAPI?"
    )

    assert answer == (
        "FastAPI is a modern Python web framework."
    )