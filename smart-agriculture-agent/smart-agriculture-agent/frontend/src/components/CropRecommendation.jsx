import { useState } from "react";
import { recommendCrop } from "../services/api";

const initial = {
  nitrogen: 90, phosphorus: 42, potassium: 43,
  temperature: 25, humidity: 80, ph: 6.5, rainfall: 200
};

export default function CropRecommendation() {
  const [form, setForm] = useState(initial);
  const [result, setResult] = useState(null);

  function updateField(e) {
    setForm({ ...form, [e.target.name]: Number(e.target.value) });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try { setResult(await recommendCrop(form)); }
    catch { setResult({ crop: "Error", confidence: 0, message: "Backend unavailable." }); }
  }

  return (
    <section className="card">
      <h2>🌱 Crop Recommendation</h2>
      <form onSubmit={handleSubmit}>
        {Object.keys(form).map((field) => (
          <input key={field} name={field} type="number" step="any"
            value={form[field]} onChange={updateField} placeholder={field} />
        ))}
        <button>Recommend Crop</button>
      </form>
      {result && <div className="result">
        <h3>Recommended Crop</h3>
        <strong>{result.crop}</strong>
        <p>Confidence: {result.confidence}%</p>
        {result.message && <p>{result.message}</p>}
      </div>}
    </section>
  );
}
