import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000"
});

export async function askAssistant(question, crop, location) {
  const response = await api.post("/api/assistant/ask", { question, crop, location });
  return response.data;
}

export async function recommendCrop(data) {
  const response = await api.post("/api/crops/recommend", data);
  return response.data;
}

export async function detectDisease(file) {
  const formData = new FormData();
  formData.append("file", file);
  const response = await api.post("/api/disease/predict", formData);
  return response.data;
}

export async function getWeather(city) {
  const response = await api.get(`/api/weather/${encodeURIComponent(city)}`);
  return response.data;
}
