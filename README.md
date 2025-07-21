# 🧠 Memora AI Assistant – Reminiscence Therapy Backend (Gemini Flash 2.0)

This is the backend API service for **Memora**, an AI-powered assistant that supports early-stage dementia and memory loss patients through conversational reminiscence therapy.

Built with **Flask** and powered by **Google Gemini Flash 2.0**, the assistant intelligently crafts personalized, empathetic responses using a knowledge base derived from user-generated memories and journaling content.

---

## 🎯 Objective

To build a reliable, empathetic backend API that:
- Uses Gemini Flash 2.0 to generate intelligent, memory-jogging responses
- Accepts a structured knowledge base and conversation history
- Returns contextual replies to support reminiscence therapy

---

## 🚀 Demo

- 🔗 [YouTube Demo Link](#) (https://youtube.com/shorts/2PIvySIlhc0?feature=share)
- 🧠 Flutter : https://github.com/Malavika-Unnikrishnan/Memora_AI_Memory_Assistant

---<img width="1113" height="553" alt="Screenshot 2025-06-08 215214" src="https://github.com/user-attachments/assets/ea827042-d1e7-4f27-a925-67df2325c6ba" />


## 🏗️ API Structure

### `POST /generate`
Generates a Gemini response using user input + knowledge base + chat history.

**Request JSON**:
```json
{
  "knowledge_base": "string",
  "conversation_history": "string",
  "user_input": "string"
}
