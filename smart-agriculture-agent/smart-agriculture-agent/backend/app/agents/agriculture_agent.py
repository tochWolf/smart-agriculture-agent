import google.generativeai as genai
from app.config import settings
from app.rag.retriever import retriever

class AgricultureAgent:
    def __init__(self):
        self.model = None
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel("gemini-2.0-flash")

    def answer(self, question, crop=None, location=None):
        context = retriever.retrieve(question)
        context_text = "\n\n".join(context)

        if self.model is None:
            return {
                "answer": "AI provider is not configured. Add GEMINI_API_KEY to backend/.env.",
                "sources": context,
            }

        prompt = f'''You are an agricultural AI assistant.
Answer the farmer's question using only the provided knowledge context where applicable.
Do not invent unsupported facts. Clearly state uncertainty.
Farmer question: {question}
Crop: {crop or "Not specified"}
Location: {location or "Not specified"}
Knowledge context:
{context_text}
Give practical, concise guidance. Do not claim to provide a definitive professional diagnosis.
'''
        response = self.model.generate_content(prompt)
        return {"answer": response.text, "sources": context}

agriculture_agent = AgricultureAgent()
