class EmployeeService:

    def __init__(self, collection):
        self.collection = collection

    def load_employees(self, employees):

        self.collection.add(
            ids=[e.id for e in employees],
            documents=[e.to_document() for e in employees],
            metadatas=[e.to_metadata() for e in employees]
        )

    def get_all(self):
        return self.collection.get()