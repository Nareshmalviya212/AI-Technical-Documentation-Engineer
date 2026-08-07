from pathlib import Path
from langchain_core.documents import Document


class DocumentLoader:

    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def load_documents(self):

        documents = []

        for file in self.data_path.rglob("*.md"):

            with open(file, "r", encoding="utf-8") as f:
                text = f.read()

            category = file.parent.name
            topic = file.stem

            document = Document(
                page_content=text,
                metadata={
                    "source_name": "FastAPI Official Documentation",
                    "source_url": "https://fastapi.tiangolo.com/",
                    "category": category,
                    "topic": topic,
                    "filename": file.name
                }
            )

            documents.append(document)

        return documents