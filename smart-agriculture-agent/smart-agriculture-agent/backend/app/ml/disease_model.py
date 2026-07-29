from pathlib import Path
import numpy as np
from PIL import Image

MODEL_PATH = Path("models/plant_disease_model.keras")
CLASSES_PATH = Path("models/classes.txt")

class DiseaseModel:
    def __init__(self):
        self.model = None
        self.class_names = []
        if MODEL_PATH.exists():
            import tensorflow as tf
            self.model = tf.keras.models.load_model(MODEL_PATH)
            if CLASSES_PATH.exists():
                self.class_names = CLASSES_PATH.read_text(encoding="utf-8").splitlines()

    def predict(self, image_path):
        if self.model is None:
            return {
                "disease": "Model not trained",
                "confidence": 0,
                "message": "Run python scripts/train_disease_model.py first."
            }

        image = Image.open(image_path).convert("RGB").resize((224, 224))
        x = np.expand_dims(np.array(image) / 255.0, axis=0)
        predictions = self.model.predict(x, verbose=0)
        index = int(np.argmax(predictions[0]))
        disease = self.class_names[index] if index < len(self.class_names) else f"class_{index}"
        return {"disease": disease, "confidence": round(float(predictions[0][index]) * 100, 2)}

disease_model = DiseaseModel()
