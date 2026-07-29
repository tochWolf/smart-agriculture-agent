from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

DATA_PATH = Path("data/crop_recommendation.csv")
MODEL_PATH = Path("models/crop_model.pkl")

def train():
    df = pd.read_csv(DATA_PATH)
    X = df.drop("label", axis=1)
    y = df["label"]

    if y.nunique() < 2:
        raise ValueError("The demo CSV contains only one class. Replace it with a complete multi-class crop dataset before training.")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"Model accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()
