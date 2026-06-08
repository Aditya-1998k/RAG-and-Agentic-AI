import os
from typing import List, Dict
from dotenv import load_dotenv
import google.genai as genai
from shared_functions import *
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# ==========================================================
# Gemini Configuration
# ==========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not found")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

food_items = []

# ==========================================================
# Main
# ==========================================================


def main():
    try:
        print("🤖 Enhanced RAG Food Chatbot")
        print("Powered by Gemini + ChromaDB")
        print("=" * 70)

        global food_items
        food_items = load_food_data("./food_data.json")
        print(f"✅ Loaded {len(food_items)} food items")

        collection = create_similarity_search_collection(
            "food_dataset",
            {"description": "Food recommendation dataset"}
        )

        initialize_collection_if_required(collection, food_items)
        print("✅ Vector database ready")

        test_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Hello, Gemini! This is a test message to verify connectivity."
        )

        if test_response.text:
            print("✅ Gemini connection successful")

        enhanced_rag_food_chatbot(collection)

    except Exception as error:
        print(f"❌ Error: {error}")


# ==========================================================
# Context Builder
# ==========================================================


def prepare_context_for_llm(query: str, search_results: List[Dict]) -> str:
    """
    Convert search results into
    Gemini-friendly context
    """
    if not search_results:
        return ("No relevant food items found.")

    context_parts = []
    context_parts.append(f"User Query: {query}\n")
    context_parts.append("Retrieved Food Items:\n")

    for index, result in enumerate(search_results[:3], start=1):
        context_parts.append(
            f"""
                Option {index}
                Food Name: {result['food_name']}
                Description: {result['food_description']}
                Cuisine: {result['cuisine_type']}
                Calories: {result['food_calories_per_serving']}
                Cooking Method: {result['cooking_method']}
                Health Benefits: {result['food_health_benefits']}
                Taste Profile: {result['taste_profile']}
                Similarity: {result['similarity_score'] * 100:.1f}%
                """
        )

    return "\n".join(context_parts)


# ==========================================================
# Gemini Response
# ==========================================================


def generate_llm_rag_response(
    query: str,
    search_results: List[Dict],
    conversation_history: List[str]
):
    """
    Generate Gemini RAG response
    """
    try:
        context = prepare_context_for_llm(query, search_results)
        history_text = "\n".join(conversation_history[-3:])

        prompt = f"""
            You are an expert food recommendation assistant.
            Conversation History: {history_text}
            Current User Query: {query}
            Retrieved Context: {context}

            Instructions:
            1. Recommend the best foods.
            2. Explain WHY they match.
            3. Mention cuisine.
            4. Mention calories.
            5. Mention health benefits.
            6. Keep response under 150 words.
            7. Be friendly and conversational.

            Answer:
        """
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        if response.text:
            return response.text

        return generate_fallback_response(
            query, search_results
        )
    except Exception as error:
        print(f"❌ Gemini Error: {error}")
        return generate_fallback_response(
            query, search_results
        )


# ==========================================================
# Fallback Response
# ==========================================================


def generate_fallback_response(query: str, search_results: List[Dict]):
    """Generate simple fallback response if LLM fails"""
    if not search_results:
        return ("I couldn't find any foods matching your request.")

    top_food = search_results[0]

    response = (
        f"Based on your request for "
        f"'{query}', "
        f"I recommend "
        f"{top_food['food_name']}."
    )

    response += f" It is a {top_food['cuisine_type']} dish"
    response += f" with {top_food['food_calories_per_serving']}  calories."
    return response


# ==========================================================
# Main Chatbot Loop
# ==========================================================


def enhanced_rag_food_chatbot(collection):
    print("\n" + "=" * 70)
    print("🤖 ENHANCED RAG FOOD CHATBOT")
    print("Powered by Gemini 2.5 Flash")
    print("=" * 70)

    print("\nExample Queries:")
    print("• healthy lunch")
    print("• spicy dinner")
    print("• protein rich breakfast")
    print("• comfort food")
    print("• low calorie snacks")
    print("\nCommands:")
    print("• help")
    print("• compare")
    print("• quit")

    print("-" * 70)

    conversation_history = []

    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            if not user_input:
                continue
            command = user_input.lower()

            if command in ["quit", "exit", "q"]:
                print( "\n🤖 Goodbye!")
                break
            elif command == "help":
                show_enhanced_rag_help()
            elif command == "compare":
                handle_comparison_mode(collection)
            else:
                handle_rag_query(
                    collection, user_input, conversation_history
                )
                conversation_history.append(user_input)

                if len(conversation_history) > 10:
                    conversation_history = conversation_history[-5:]

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as error:
            print(f"❌ Error: {error}")


# ==========================================================
# Query Handler
# ==========================================================


def handle_rag_query(collection, query, conversation_history):
    """Handle user query with RAG flow"""
    print("\n🔍 Searching vector database...")

    search_results = perform_similarity_search(
        collection,
        query, 5
    )

    if not search_results:
        print("\n🤖 No matching foods found.")
        return
    print("🧠 Generating Gemini response...")

    response = generate_llm_rag_response(
        query,
        search_results,
        conversation_history
    )

    print(f"\n🤖 {response}")
    print("\n📊 Retrieved Results")
    print("-" * 50)

    for index, result in enumerate(search_results[:3], start=1):
        print(f"\n{index}. {result['food_name']}")
        print(f"   Cuisine: {result['cuisine_type']}")
        print(f"   Calories: {result['food_calories_per_serving']}")
        print(f"   Similarity: {result['similarity_score'] * 100:.1f}%")


# ==========================================================
# Comparison Mode
# ==========================================================


def handle_comparison_mode(collection):
    """Handle comparison mode where user can compare two queries"""
    print("\n🔄 COMPARISON MODE")

    query1 = input("First query: ").strip()
    query2 = input("Second query: ").strip()

    if not query1 or not query2:
        return

    results1 = perform_similarity_search(
        collection, query1, 3
    )
    results2 = perform_similarity_search(
        collection, query2, 3
    )

    comparison_prompt = f"""
        Compare these food preferences.
        Query 1: {query1}
        Top Recommendation: {results1[0]['food_name'] if results1 else 'None'}
        Query 2: {query2}
        Top Recommendation: {results2[0]['food_name'] if results2 else 'None'}
        Provide a concise comparison.
        """

    response = model.generate_content(
        comparison_prompt
    )
    print("\n🤖 Gemini Analysis:")
    print(response.text)


# ==========================================================
# Help
# ==========================================================

def show_enhanced_rag_help():
    print("\n📖 HELP")
    print("=" * 50)
    print("Ask questions naturally.")
    print("\nExamples:")
    print("• healthy lunch")
    print("• spicy dinner")
    print("• high protein breakfast")
    print("• low calorie snacks")
    print("\nCommands:")
    print("• compare")
    print("• help")
    print("• quit")


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()