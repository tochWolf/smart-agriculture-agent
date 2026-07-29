from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.routes import crops, disease, weather, assistant

app = FastAPI(title=settings.APP_NAME, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(crops.router)
app.include_router(disease.router)
app.include_router(weather.router)
app.include_router(assistant.router)

@app.get("/")
def root():
    return {"message": "Smart Agriculture AI API", "status": "running"}
