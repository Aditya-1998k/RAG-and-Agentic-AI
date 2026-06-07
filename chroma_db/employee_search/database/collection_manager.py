from config.settings import COLLECTION_NAME


class CollectionManager:

    def __init__(self, client, embedding_function):
        self.client = client
        self.embedding_function = embedding_function

    def create_collection(self):
        return self.client.create_collection(
            name=COLLECTION_NAME,
            metadata={
                "description": "Employee Search Collection"
            },
            configuration={
                "hnsw": {
                    "space": "cosine"
                },
                "embedding_function": self.embedding_function
            }
        )