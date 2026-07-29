import tempfile
from fastapi import APIRouter, UploadFile, File
from app.ml.disease_model import disease_model

router = APIRouter(prefix="/api/disease", tags=["Disease Detection"])

@router.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    content = await file.read()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        temp.write(content)
        path = temp.name
    return disease_model.predict(path)
