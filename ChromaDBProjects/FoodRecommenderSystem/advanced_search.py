from shared_functions import *


def main():
    """
    Main function for advanced search system
    """
    try:
        print("🔬 Advanced Food Search System")
        print("=" * 60)
        print("Loading food database...")
        food_items = load_food_data("./food_data.json")
        print(f"✅ Loaded {len(food_items)} food items")

        collection = create_similarity_search_collection(
            "food_dataset", {"description": "Food recommendation collection"}
        )

        initialize_collection_if_required(collection, food_items)
        interactive_advanced_search(collection)
    except Exception as error:
        print(f"❌ Initialization Error: {error}")


# ------------------------------------------------------------------
# Menu
# ------------------------------------------------------------------


def interactive_advanced_search(collection):
    """Advanced search menu"""

    while True:
        print("\n" + "=" * 60)
        print("🔧 ADVANCED FOOD SEARCH")
        print("=" * 60)

        print("1. Basic Similarity Search")
        print("2. Cuisine Filtered Search")
        print("3. Calorie Filtered Search")
        print("4. Cooking Method Search")
        print("5. Combined Filters Search")
        print("6. Demonstration Mode")
        print("7. Help")
        print("8. Exit")

        print("-" * 60)

        try:
            choice = input("\n📋 Select option: ").strip()

            if choice == "1":
                perform_basic_search(collection)
            elif choice == "2":
                perform_cuisine_filtered_search(collection)
            elif choice == "3":
                perform_calorie_filtered_search(collection)
            elif choice == "4":
                perform_cooking_method_search(collection)
            elif choice == "5":
                perform_combined_filtered_search(collection)
            elif choice == "6":
                run_search_demonstrations(collection)
            elif choice == "7":
                show_advanced_help()
            elif choice == "8":
                print("\n👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as error:
            print(f"❌ Error: {error}")


# ------------------------------------------------------------------
# Basic Search
# ------------------------------------------------------------------


def perform_basic_search(collection):
    """Basic semantic search"""
    print("\n🔍 BASIC SEARCH")

    query = input("Enter search query: ").strip()

    if not query:
        print("❌ Query required")
        return

    results = perform_similarity_search(
        collection, query, 5
    )

    display_search_results(
        results, "Basic Search Results"
    )


# ------------------------------------------------------------------
# Cuisine Filter Search
# ------------------------------------------------------------------


def perform_cuisine_filtered_search(collection):
    """Cuisine based search"""
    cuisines = [
        "Italian", "Thai", "Mexican", "Indian", "Japanese", "French",
        "Mediterranean", "American", "Health Food", "Dessert"
    ]

    print("\n🍽️ CUISINE FILTER SEARCH")
    print("\nAvailable Cuisines:")

    for index, cuisine in enumerate(cuisines, start=1):
        print(f"{index}. {cuisine}")

    query = input("\nEnter query: ").strip()
    cuisine_input = input("Cuisine: ").strip()

    if not query:
        print("❌ Query required")
        return

    cuisine_filter = None

    if cuisine_input.isdigit():
        index = int(cuisine_input) - 1

        if (0 <= index < len(cuisines)):
            cuisine_filter = cuisines[index]
    else:
        cuisine_filter = cuisine_input

    results = perform_filtered_similarity_search(
        collection, query, cuisine_filter=cuisine_filter, n_results=5
    )

    display_search_results( results, f"Cuisine Filter: {cuisine_filter}")


# ------------------------------------------------------------------
# Calorie Filter Search
# ------------------------------------------------------------------


def perform_calorie_filtered_search(collection):
    """Search with calorie limit"""
    print("\n🔥 CALORIE FILTER SEARCH")

    query = input("Enter query: ").strip()
    calorie_input = input("Maximum calories: ").strip()

    if not query:
        print("❌ Query required")
        return

    max_calories = None
    if calorie_input.isdigit():
        max_calories = int(calorie_input)

    results = perform_filtered_similarity_search(
        collection, query, max_calories=max_calories, n_results=5
    )

    display_search_results(
        results,
        f"Under {max_calories} Calories"
    )


# ------------------------------------------------------------------
# Cooking Method Search
# ------------------------------------------------------------------


def perform_cooking_method_search(collection):
    """Search by cooking method"""
    print("\n👨‍🍳 COOKING METHOD SEARCH")
    print("\nExamples:")

    print("• Baking")
    print("• Grilling")
    print("• Roasting")
    print("• Steaming")

    query = input("\nEnter query: ").strip()
    cooking_method = input("Cooking method: ").strip()

    if not query:
        print("❌ Query required")
        return

    results = perform_filtered_similarity_search(
        collection, query, cooking_method_filter=cooking_method, n_results=5
    )

    display_search_results(
        results,
        f"Cooking Method: {cooking_method}"
    )


# ------------------------------------------------------------------
# Combined Search
# ------------------------------------------------------------------


def perform_combined_filtered_search(collection):
    """Combined filters"""
    print("\n🎯 COMBINED FILTER SEARCH")
    query = input("Enter query: ").strip()
    cuisine = input("Cuisine (optional): ").strip()
    calories = input("Max calories (optional): ").strip()
    cooking_method = input("Cooking method (optional): ").strip()

    if not query:
        print("❌ Query required")
        return

    max_calories = None
    if calories.isdigit():
        max_calories = int(calories)

    results = perform_filtered_similarity_search(
        collection, query,
        cuisine_filter=(cuisine if cuisine else None),
        max_calories=max_calories,
        cooking_method_filter=(cooking_method if cooking_method else None),
        n_results=5
    )

    display_search_results(
        results,
        "Combined Filter Results"
    )


# ------------------------------------------------------------------
# Demonstrations
# ------------------------------------------------------------------


def run_search_demonstrations(collection):
    """Predefined demos"""
    demonstrations = [
        {
            "title": "Italian Pasta Search",
            "query": "creamy pasta",
            "cuisine": "Italian", 
            "calories": None,
            "method": None
        },
        {
            "title": "Healthy Low-Calorie Search",
            "query": "healthy meal",
            "cuisine": None,
            "calories": 300,
            "method":  None
        },
        {
            "title": "Grilled Healthy Food",
            "query": "healthy protein",
            "cuisine": None,
            "calories": 400,
            "method": "Grilling"
        }
    ]

    print( "\n📊 DEMONSTRATION MODE")

    for demo in demonstrations:
        print("\n" + "=" * 60)
        print(demo["title"])
        print("=" * 60)

        results = perform_filtered_similarity_search(
            collection,
            query=demo["query"],
            cuisine_filter=demo["cuisine"],
            max_calories=demo["calories"],
            cooking_method_filter=demo["method"],
            n_results=3
        )

        display_search_results(
            results,
            demo["title"],
            show_details=False
        )

        input("\n⏸️ Press Enter to continue...")


# ------------------------------------------------------------------
# Display Results
# ------------------------------------------------------------------


def display_search_results(results, title, show_details=True):
    """Display formatted results"""
    print(f"\n📋 {title}")
    print("=" * 70)
    if not results:
        print("❌ No matching results found")
        return

    for index, result in enumerate(results, start=1):
        score = (result["similarity_score"] * 100)

        if show_details:
            print(f"\n{index}. 🍽️ {result['food_name']}")
            print(f"   📊 Similarity: {score:.1f}%")
            print(f"   🏷️ Cuisine: {result['cuisine_type']}")
            print(f"   🔥 Calories: {result['food_calories_per_serving']}")
            print(f"   👨‍🍳 Method: {result['cooking_method']}")
            print(f"   📝 {result['food_description']}")
        else:
            print(f"{index}. {result['food_name']} ({score:.1f}%)")

    print("\n" + "=" * 70)


# ------------------------------------------------------------------
# Help
# ------------------------------------------------------------------


def show_advanced_help():
    """Help menu"""
    print("\n📖 ADVANCED SEARCH HELP")
    print("=" * 60)

    print("\nAvailable Search Modes:")

    print("1. Basic Search")
    print("2. Cuisine Filtering")
    print("3. Calorie Filtering")
    print("4. Cooking Method Filtering")
    print("5. Combined Filters")
    print("6. Demonstrations")
    print("\nExample Queries:")
    print("• chocolate dessert")
    print("• healthy breakfast")
    print("• spicy dinner")
    print("• grilled chicken")
    print("• baked sweets")
    print("\nTips:")
    print("• Use natural descriptions")
    print("• Try ingredients and cuisines")
    print("• Combine filters for precision")


if __name__ == "__main__":
    main()