from shared_functions import *

food_items = []
search_history = []


def main():
    """
    Main function for interactive food recommendation system
    """
    try:
        print("🍽️ Interactive Food Recommendation System")
        print("=" * 60)
        print("Loading food database...")
        global food_items

        food_items = load_food_data("./food_data.json")

        print(f"✅ Loaded {len(food_items)} food items")

        collection = create_similarity_search_collection(
            "interactive_food_search",
            {"description": "Interactive food search collection"}
        )

        populate_similarity_collection(collection, food_items)
        interactive_food_chatbot(collection)
    except Exception as error:
        print(f"❌ Initialization Error: {error}")


def interactive_food_chatbot(collection):
    """
    Interactive CLI search interface
    """
    print("\n" + "=" * 60)
    print("🤖 FOOD SEARCH CHATBOT")
    print("=" * 60)

    print("Available Commands:")

    print("  • Type any food query")
    print("  • help     -> Show help")
    print("  • history  -> Show search history")
    print("  • quit     -> Exit")

    print("-" * 60)

    while True:
        try:
            user_input = input("\n🔍 Search food: ").strip()
            if not user_input:
                print("⚠️ Please enter a search query")
                continue

            command = user_input.lower()

            if command in ["quit", "exit", "q"]:
                print("\n👋 Thank you for using Food Search!")
                break

            elif command in ["help", "h"]:
                show_help_menu()

            elif command == "history":
                show_search_history()

            else:
                search_history.append(user_input)
                handle_food_search(collection, user_input)

        except KeyboardInterrupt:
            print( "\n\n👋 Goodbye!")
            break

        except Exception as error:
            print(f"❌ Error: {error}")


def show_help_menu():
    """Display help information"""
    print("\n📖 HELP MENU")
    print("-" * 40)
    print("Example Searches:")

    print("  • chocolate dessert")
    print("  • italian food")
    print("  • healthy breakfast")
    print("  • spicy dinner")
    print("  • baked goods")
    print("  • protein rich meal")
    print("  • low calorie snack")

    print("\nCommands:")

    print("  • help")
    print("  • history")
    print("  • quit")


def show_search_history():
    """Display search history"""
    print("\n🕒 SEARCH HISTORY")
    print("-" * 40)

    if not search_history:
        print("No searches yet.")
        return

    for index, query in enumerate(search_history, start=1):
        print(f"{index}. {query}")


def handle_food_search(collection, query):
    """Handle food similarity search"""

    print(f"\n🔍 Searching for '{query}'...")

    results = perform_similarity_search(collection, query, 5)

    if not results:
        print("\n❌ No matching foods found.")
        print("\n💡 Suggestions:")

        print("  • chocolate")
        print("  • italian")
        print("  • dessert")
        print("  • grilled")
        print("  • spicy")
        return

    display_search_results(results)
    suggest_related_searches(results)


def display_search_results(results):
    """Display formatted results"""
    print("\n✅ Search Results")
    print("=" * 70)

    # Top recommendation
    best_match = results[0]
    print("⭐ TOP RECOMMENDATION")
    print(f"🍽️ {best_match['food_name']}")

    print(
        f"📊 Match Score: "
        f"{best_match['similarity_score'] * 100:.1f}%"
    )

    print(f"🏷️ Cuisine: {best_match['cuisine_type']}")
    print(f"🔥 Calories: {best_match['food_calories_per_serving']}")

    print("-" * 70)
    print("\n📋 All Matches")

    for index, result in enumerate(results, start=1):
        score = (result["similarity_score"] * 100)

        print(f"\n{index}. 🍽️ {result['food_name']}")
        print(f"    📊 Match: {score:.1f}%")
        print(f"    🏷️ Cuisine: {result['cuisine_type']}")
        print(f"    🔥 Calories: {result['food_calories_per_serving']}")
        print(f"    👨‍🍳 Cooking: {result['cooking_method']}")

        description = result["food_description"]

        if len(description) > 150:
            description = (description[:150] + "...")
        print(f"    📝 {description}")

    print("\n" + "=" * 70)


def suggest_related_searches(results):
    """Suggest additional searches"""
    if not results:
        return
    print("\n💡 Related Searches")

    cuisines = list(set([r["cuisine_type"] for r in results]))

    for cuisine in cuisines[:3]:
        print(f"   • {cuisine} dishes")

    avg_calories = sum([r["food_calories_per_serving"] for r in results]) / len(results)

    if avg_calories > 350:
        print("   • low calorie meals")
        print("   • healthy alternatives")
    else:
        print("   • hearty meals")
        print("   • comfort food")

if __name__ == "__main__":
    main()