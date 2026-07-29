from pathlib import Path
import tensorflow as tf

DATASET_PATH = "data/plant_disease"
MODEL_PATH = Path("models/plant_disease_model.keras")
CLASS_PATH = Path("models/classes.txt")

def train():
    train_ds = tf.keras.utils.image_dataset_from_directory(
        DATASET_PATH, image_size=(224, 224), batch_size=32,
        validation_split=0.2, subset="training", seed=42
    )
    validation_ds = tf.keras.utils.image_dataset_from_directory(
        DATASET_PATH, image_size=(224, 224), batch_size=32,
        validation_split=0.2, subset="validation", seed=42
    )

    class_names = train_ds.class_names
    print("Classes:", class_names)

    augmentation = tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal"),
        tf.keras.layers.RandomRotation(0.1),
        tf.keras.layers.RandomZoom(0.1),
    ])

    base_model = tf.keras.applications.MobileNetV2(
        input_shape=(224, 224, 3), include_top=False, weights="imagenet"
    )
    base_model.trainable = False

    model = tf.keras.Sequential([
        augmentation,
        tf.keras.layers.Rescaling(1.0 / 255),
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(len(class_names), activation="softmax"),
    ])

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(train_ds, validation_data=validation_ds, epochs=10)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    model.save(MODEL_PATH)
    CLASS_PATH.write_text("\n".join(class_names), encoding="utf-8")
    print("Disease model saved.")

if __name__ == "__main__":
    train()
