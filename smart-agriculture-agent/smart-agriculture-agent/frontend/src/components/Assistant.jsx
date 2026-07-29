import { useState } from "react";
import { askAssistant } from "../services/api";

export default function Assistant() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleAsk() {
    if (!question.trim()) return;
    setLoading(true);
    try {
      const result = await askAssistant(question);
      setAnswer(result.answer);
    } catch {
      setAnswer("Unable to connect to AI assistant.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="card wide">
      <h2>🤖 AI Agriculture Assistant</h2>
      <textarea value={question} onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask about crops, soil, diseases, irrigation..." />
      <button onClick={handleAsk}>{loading ? "Thinking..." : "Ask AI"}</button>
      {answer && <div className="answer"><h3>AI Recommendation</h3><p>{answer}</p></div>}
    </section>
  );
}
