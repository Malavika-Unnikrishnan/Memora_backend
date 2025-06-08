from flask import Flask, request, jsonify
from google import genai
import os

app = Flask(__name__)

# Set your Gemini API key here or via environment variable


client = genai.Client(api_key="GEMINI_API_KEY")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    kb = data.get("knowledge_base", "")
    history = data.get("conversation_history", "")
    user_input = data.get("user_input", "")

    if user_input.strip().lower() == "hi":
        prompt = f"""
You are an empathetic AI assistant engaging in reminiscence therapy with a dementia patient. Based on the following knowledge base, start a warm, friendly conversation by asking one thoughtful question that may help the user recall a positive memory or recent event. Only output your message — no explanation, no labels.

Knowledge Base:
\"\"\"{kb}\"\"\"

Gemini:"""
    else:
        prompt = f"""
You are an empathetic AI assistant continuing a reminiscence therapy conversation with a dementia patient. Use the knowledge base and conversation history to craft a warm, engaging reply that helps the user recall meaningful experiences. Only respond with the next line Gemini should say. No extra explanation, no labels.

Knowledge Base:
\"\"\"{kb}\"\"\"

Conversation History:
\"\"\"{history}
User: {user_input}
Gemini:\"\"\"

Now continue the conversation.
"""

    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt
)
    return jsonify({"response": response.text})


@app.route("/", methods=["GET"])
def health_check():
    return "Gemini API backend is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
