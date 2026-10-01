
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

CONFIDENCE_THRESHOLD = 60.0
GREEN_RATIO_THRESHOLD = 0.03


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


model, class_names = load_model()


# ==========================================
# CHECK IF IMAGE LOOKS PLANT-LIKE
# ==========================================

def looks_like_plant_image(image):

    image = image.resize((100, 100)).convert("RGB")
    pixels = list(image.getdata())

    green_pixels = 0
    natural_pixels = 0

    for r, g, b in pixels:

        if (
            g > r * 1.05
            and g > b * 1.05
            and g > 50
        ):
            green_pixels += 1

        maximum = max(r, g, b)
        minimum = min(r, g, b)

        if maximum - minimum > 30:
            natural_pixels += 1

    total_pixels = len(pixels)

    green_ratio = green_pixels / total_pixels
    natural_ratio = natural_pixels / total_pixels

    return (
        green_ratio >= GREEN_RATIO_THRESHOLD
        or natural_ratio >= 0.20
    )


# ==========================================
# PREDICT DISEASE
# ==========================================

def predict_disease(image):

    if not isinstance(image, Image.Image):
        image = Image.open(image)

    image = image.convert("RGB")

    # Reject images that do not look plant-like
    if not looks_like_plant_image(image):
        return "NOT_A_PLANT", 0.0

    image_tensor = transform(image)
    image_tensor = image_tensor.unsqueeze(0)
    image_tensor = image_tensor.to(DEVICE)

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
    confidence_percentage = confidence.item() * 100

    # Low confidence: plant image, but model is unsure
    if confidence_percentage < CONFIDENCE_THRESHOLD:
        return "UNSUPPORTED_PLANT", confidence_percentage

    disease_name = class_names[predicted_index]

    return disease_name, confidence_percentage