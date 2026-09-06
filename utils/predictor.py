import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image


# ==========================================
# SETTINGS
# ==========================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "crop_disease_model.pth"
)

IMAGE_SIZE = 224

DEVICE = torch.device("cpu")


# ==========================================
# IMAGE TRANSFORMATION
# ==========================================

transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
    )
])


# ==========================================
# LOAD MODEL
# ==========================================

def load_model():

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model not found at: {MODEL_PATH}"
        )

    checkpoint = torch.load(
        MODEL_PATH,
        map_location=DEVICE
    )

    class_names = checkpoint["classes"]

    model = models.mobilenet_v3_small(
        weights=None
    )

    model.classifier[3] = nn.Linear(
        model.classifier[3].in_features,
        len(class_names)
    )

    model.load_state_dict(
        checkpoint["model_state"]
    )

    model = model.to(DEVICE)

    model.eval()

    return model, class_names


# ==========================================
# LOAD MODEL ONCE
# ==========================================

model, class_names = load_model()


# ==========================================
# PREDICT DISEASE
# ==========================================

def predict_disease(image):

    if not isinstance(image, Image.Image):
        image = Image.open(image)

    image = image.convert("RGB")

    image_tensor = transform(image)

    image_tensor = image_tensor.unsqueeze(0)

    image_tensor = image_tensor.to(DEVICE)

    # ======================================
    # PREDICTION
    # ======================================

    with torch.no_grad():

        outputs = model(image_tensor)

        probabilities = torch.softmax(
            outputs,
            dim=1
        )

        confidence, predicted_index = torch.max(
            probabilities,
            dim=1
        )

    predicted_index = predicted_index.item()

    confidence = confidence.item()

    disease_name = class_names[predicted_index]

    confidence_percentage = confidence * 100

    return disease_name, confidence_percentage