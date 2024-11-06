import chromadb
from chromadb.config import Settings
from typing import List

class VectorDB:
    def __init__(self):
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory="./data/vectordb"
        ))
        self.collection = self.client.get_or_create_collection("questions")

    def add_questions(self, questions: List[str], metadata: List[dict]):
        self.collection.add(
            documents=questions,
            metadatas=metadata,
            ids=[f"q_{i}" for i in range(len(questions))]
        )

    def search_similar(self, query: str, n_results: int = 5):
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results