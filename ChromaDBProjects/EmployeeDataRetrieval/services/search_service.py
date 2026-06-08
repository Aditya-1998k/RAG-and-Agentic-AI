class SearchService:

    def __init__(self, collection):
        self.collection = collection

    def semantic_search(
        self,
        query,
        n_results=5,
        where=None
    ):
        return self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where
        )

    def filter_by_department(self, department):
        return self.collection.get(
            where={
                "department": department
            }
        )

    def filter_by_experience(self, years):
        return self.collection.get(
            where={
                "experience": {
                    "$gte": years
                }
            }
        )

    def filter_by_location(self, locations):
        return self.collection.get(
            where={
                "location": {
                    "$in": locations
                }
            }
        )