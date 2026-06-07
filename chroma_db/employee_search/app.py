from data.employee import employees
from embeddings.embeddings_factory import get_embedding_function
from database.chromadb_client import get_client
from database.collection_manager import CollectionManager
from services.employee_service import EmployeeService
from services.search_service import SearchService


def main():

    client = get_client()

    embedding_fn = get_embedding_function()

    collection = CollectionManager(
        client,
        embedding_fn
    ).create_collection()

    employee_service = EmployeeService(collection)
    employee_service.load_employees(employees)

    search_service = SearchService(collection)

    results = search_service.semantic_search(
        "Python developer with web experience",
        n_results=3
    )

    print(results)


if __name__ == "__main__":
    main()