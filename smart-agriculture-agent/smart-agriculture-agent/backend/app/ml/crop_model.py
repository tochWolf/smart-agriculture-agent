from pathlib import Path
import joblib
import numpy as np

MODEL_PATH = Path("models/crop_model.pkl")

class CropModel:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH) if MODEL_PATH.exists() else None

    def predict(self, features: list[float]):
        if self.model is None:
            return {
                "crop": "Model not trained",
                "confidence": 0,
                "message": "Run python scripts/train_crop_model.py first."
            }

        x = np.array(features).reshape(1, -1)
        prediction = self.model.predict(x)[0]
        confidence = float(np.max(self.model.predict_proba(x))) * 100 if hasattr(self.model, "predict_proba") else 0

        return {"crop": str(prediction), "confidence": round(confidence, 2)}

crop_model = CropModel()
