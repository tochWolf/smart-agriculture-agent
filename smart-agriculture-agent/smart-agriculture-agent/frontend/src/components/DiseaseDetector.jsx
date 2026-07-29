import { useState } from "react";
import { detectDisease } from "../services/api";

export default function DiseaseDetector() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit() {
    if (!file) return;
    setLoading(true);
    try { setResult(await detectDisease(file)); }
    catch { setResult({ disease: "Error", confidence: 0, message: "Unable to analyse image." }); }
    finally { setLoading(false); }
  }

  return (
    <section className="card">
      <h2>🍃 Plant Disease Detector</h2>
      <input type="file" accept="image/*" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleSubmit}>{loading ? "Analysing..." : "Detect Disease"}</button>
      {result && <div className="result">
        <h3>{result.disease}</h3>
        <p>Confidence: {result.confidence}%</p>
        {result.message && <p>{result.message}</p>}
      </div>}
    </section>
  );
}
