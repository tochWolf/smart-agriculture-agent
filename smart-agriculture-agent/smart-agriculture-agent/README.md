# 🌱 Smart Agriculture AI

A VS Code-ready AI/ML agriculture platform with crop recommendation, plant disease detection, weather intelligence, RAG-based agricultural knowledge retrieval, and an AI assistant.

## Features

- Crop recommendation using Random Forest
- Plant disease detection using MobileNetV2 transfer learning
- RAG-style agriculture knowledge retrieval
- Gemini-powered agriculture assistant
- OpenWeather integration
- React + Vite frontend
- FastAPI backend
- Docker Compose setup

## Requirements

- Python 3.11 recommended
- Node.js 20+
- VS Code
- Optional Gemini API key
- Optional OpenWeather API key

## Setup

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

Backend: http://localhost:8000
Swagger: http://localhost:8000/docs

### Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:5173

## Crop Model

Replace `backend/data/crop_recommendation.csv` with a complete multi-class crop recommendation dataset containing:

`N,P,K,temperature,humidity,ph,rainfall,label`

Then run:

```bash
cd backend
python scripts/train_crop_model.py
```

## Disease Model

Place a labelled image dataset at:

```text
backend/data/plant_disease/
  Class_A/
  Class_B/
  Class_C/
```

Then run:

```bash
cd backend
python scripts/train_disease_model.py
```

The trained model and classes are saved under `backend/models/`.

## Environment Variables

Copy `.env.example` to `.env` and configure:

- `GEMINI_API_KEY`
- `WEATHER_API_KEY`
- `FRONTEND_URL`

Without API keys, the core application still runs, but live weather and Gemini responses are unavailable.

## Docker

Create `backend/.env`, then run from the project root:

```bash
docker compose up --build
```

## Notes

The included crop CSV is intentionally tiny and is only a smoke-test example. It is not sufficient to train a reliable crop recommendation model. Replace it with a complete, properly licensed dataset before training.

Disease predictions are probabilistic and should not be treated as definitive agricultural diagnosis.
