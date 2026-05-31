import gradio as gr
import requests

API_URL = "http://localhost:8000/query"


def chat(message, history):

    response = requests.post(
        API_URL,
        json={
            "question": message
        }
    )

    result = response.json()

    return result["answer"]


demo = gr.ChatInterface(
    fn=chat,
    title="Insurance RAG Assistant",
    description="Ask questions from indexed documents"
)

demo.launch()