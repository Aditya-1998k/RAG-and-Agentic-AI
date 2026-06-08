import json
from typing import List, Dict, Optional

import chromadb
from chromadb.utils import embedding_functions

# ------------------------------------------------------------------
# ChromaDB Setup
# ------------------------------------------------------------------

client = chromadb.PersistentClient(
    path="./chroma_db"
)

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="BAAI/bge-base-en-v1.5"
)

# ------------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------------


def load_food_data(file_path: str) -> List[Dict]:
    """
    Load and normalize food dataset
    Each food item is expected to have:
        - food_id (string)
        - food_name (string)
        - food_description (string)
        - food_ingredients (list of strings)
        - cuisine_type (string)
        - food_calories_per_serving (number)
        - food_health_benefits (string)
        - cooking_method (string)
        - food_features (dict of taste features)
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            food_data = json.load(file)

        for index, item in enumerate(food_data):
            item["food_id"] = str(
                item.get(
                    "food_id",
                    index + 1
                )
            )

            item.setdefault("food_name", "Unknown Food")
            item.setdefault("food_description", "")
            item.setdefault("food_ingredients", [])
            item.setdefault("cuisine_type", "Unknown")
            item.setdefault("food_calories_per_serving", 0)
            item.setdefault("food_health_benefits", "")
            item.setdefault("cooking_method", "")

            # Build taste profile
            taste_profile = []

            food_features = item.get(
                "food_features",
                {}
            )

            if isinstance(food_features, dict):
                for value in food_features.values():
                    if value:
                        taste_profile.append(
                            str(value)
                        )

            item["taste_profile"] = ", ".join(taste_profile)

        print(f"✅ Loaded {len(food_data)} food items")

        return food_data

    except Exception as error:
        print(f"❌ Error loading dataset: {error}")
        return []


# ------------------------------------------------------------------
# Collection Creation
# ------------------------------------------------------------------


def create_similarity_search_collection(
    collection_name: str,
    collection_metadata: dict = None
):
    """Create Chroma collection"""
    try:
        collection = client.get_collection(
            name=collection_name,
            embedding_function=embedding_function
        )
        print(
            f"✅ Existing collection found: "
            f"{collection_name}"
        )

        print(
            f"📦 Documents in collection: "
            f"{collection.count()}"
        )

        return collection

    except Exception:
        print(
            f"🆕 Creating new collection: "
            f"{collection_name}"
        )

        collection = client.create_collection(
            name=collection_name,
            metadata=collection_metadata,
            embedding_function=embedding_function
        )

        return collection


# ------------------------------------------------------------------
# Populate Collection
# ------------------------------------------------------------------


def populate_similarity_collection(collection, food_items: List[Dict]):
    """
    Populate collection with food documents
    """
    ids = []
    documents = []
    metadatas = []
    used_ids = set()

    for index, food in enumerate(food_items):
        document = f"""
        Food Name: {food['food_name']}
        Description: {food['food_description']}
        Cuisine: {food['cuisine_type']}
        Ingredients: {", ".join(food['food_ingredients'])}
        Health Benefits: {food['food_health_benefits']}
        Cooking Method: {food['cooking_method']}
        Calories: {food['food_calories_per_serving']}
        Taste Profile: {food['taste_profile']}
        """

        base_id = food["food_id"]
        unique_id = base_id
        counter = 1
        while unique_id in used_ids:
            unique_id = f"{base_id}_{counter}"
            counter += 1

        used_ids.add(unique_id)
        ids.append(unique_id)
        documents.append(document)

        metadatas.append(
            {
                "name": food["food_name"],
                "description": food["food_description"],
                "cuisine_type": food["cuisine_type"],
                "calories": food["food_calories_per_serving"],
                "ingredients": ", ".join(food["food_ingredients"]),
                "health_benefits": food["food_health_benefits"],
                "cooking_method": food["cooking_method"],
                "taste_profile": food["taste_profile"],
            }
        )

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )

    print(f"✅ Indexed {len(food_items)} food items")


# ------------------------------------------------------------------
# Similarity Search
# ------------------------------------------------------------------


def perform_similarity_search(collection, query: str, n_results: int = 5):
    """
    Basic semantic similarity search
    """
    try:
        results = collection.query(
            query_texts=[query],
            n_results=n_results
        )

        if (
            not results
            or not results["ids"]
            or len(results["ids"][0]) == 0
        ):
            return []

        formatted_results = []

        for index in range(len(results["ids"][0])):
            distance = results["distances"][0][index]
            similarity_score = 1 - distance
            metadata = results["metadatas"][0][index]

            formatted_results.append(
                {
                    "food_id": results["ids"][0][index],
                    "food_name": metadata["name"],
                    "food_description": metadata["description"],
                    "cuisine_type": metadata["cuisine_type"],
                    "food_calories_per_serving": metadata["calories"],
                    "food_health_benefits": metadata["health_benefits"],
                    "cooking_method": metadata["cooking_method"],
                    "ingredients": metadata["ingredients"],
                    "taste_profile": metadata["taste_profile"],
                    "similarity_score": similarity_score,
                    "distance": distance,
                }
            )
        return formatted_results
    except Exception as error:
        print(f"❌ Search Error: {error}")
        return []


# ------------------------------------------------------------------
# Advanced Search
# ------------------------------------------------------------------


def perform_filtered_similarity_search(
    collection,
    query: str,
    cuisine_filter: Optional[str] = None,
    max_calories: Optional[int] = None,
    cooking_method_filter: Optional[str] = None,
    n_results: int = 5
):
    """Similarity search + metadata filtering"""

    filters = []
    if cuisine_filter:
        filters.append({"cuisine_type": cuisine_filter})
    if max_calories:
        filters.append({"calories": {"$lte": max_calories}})

    if cooking_method_filter:
        filters.append({"cooking_method": cooking_method_filter})

    where_clause = None

    if len(filters) == 1:
        where_clause = filters[0]

    elif len(filters) > 1:
        where_clause = {"$and": filters}

    try:
        results = collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where_clause
        )

        if (
            not results
            or not results["ids"]
            or len(results["ids"][0]) == 0
        ):
            return []

        formatted_results = []

        for index in range(len(results["ids"][0])):
            distance = results["distances"][0][index]
            similarity_score = 1 - distance
            metadata = results["metadatas"][0][index]

            formatted_results.append(
                {
                    "food_id": results["ids"][0][index],
                    "food_name": metadata["name"],
                    "food_description": metadata["description"],
                    "cuisine_type": metadata["cuisine_type"],
                    "food_calories_per_serving": metadata["calories"],
                    "food_health_benefits": metadata["health_benefits"],
                    "cooking_method": metadata["cooking_method"],
                    "ingredients": metadata["ingredients"],
                    "taste_profile": metadata["taste_profile"],
                    "similarity_score": similarity_score,
                    "distance": distance,
                }
            )
        return formatted_results
    except Exception as error:
        print(f"❌ Filter Search Error: {error}")
        return []

def initialize_collection_if_required(
    collection,
    food_items
):
    if collection.count() > 0:
        print(
            f"✅ Existing collection found with "
            f"{collection.count()} documents"
        )
        return

    print("📥 Collection empty. Creating embeddings...")
    populate_similarity_collection(collection, food_items)
