from fastapi import APIRouter
from app.schemas import CropRequest
from app.ml.crop_model import crop_model

router = APIRouter(prefix="/api/crops", tags=["Crops"])

@router.post("/recommend")
def recommend_crop(request: CropRequest):
    features = [
        request.nitrogen, request.phosphorus, request.potassium,
        request.temperature, request.humidity, request.ph, request.rainfall
    ]
    return crop_model.predict(features)
