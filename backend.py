from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import json

from utils.predictor import predict_disease


# ==========================================
# CREATE FASTAPI APP
# ==========================================

app = FastAPI(
    title="AI Crop Disease Detection API",
    description="AI-powered crop disease detection system",
    version="1.0"
)


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# LOAD DISEASE INFORMATION
# ==========================================

try:

    with open(
        "disease_info.json",
        "r",
        encoding="utf-8"
    ) as file:

        disease_info = json.load(file)

except Exception as e:

    print("⚠️ Could not load disease_info.json:")
    print(e)

    disease_info = {}


# ==========================================
# HOME / TEST ROUTE
# ==========================================

@app.get("/")
def home():

    return {
        "message": "🌱 AI Crop Disease Detection API is running!",
        "status": "success"
    }


# ==========================================
# DISEASE DETECTION
# ==========================================

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    try:

        print("\n📷 Image received:", file.filename)

        # --------------------------------------
        # READ IMAGE
        # --------------------------------------

        image_bytes = await file.read()

        print("✅ Image received successfully")

        image = Image.open(
            io.BytesIO(image_bytes)
        ).convert("RGB")

        print("✅ Image converted to RGB")


        # --------------------------------------
        # AI PREDICTION
        # --------------------------------------

        print("🤖 Running AI prediction...")

        disease_name, confidence = predict_disease(
            image
        )

        print("🌱 Prediction:", disease_name)
        print("📊 Confidence:", confidence)


        # --------------------------------------
        # GET DISEASE INFORMATION
        # --------------------------------------

        info = disease_info.get(
            disease_name,
            {}
        )


        # --------------------------------------
        # RETURN RESULT
        # --------------------------------------

        return {

            "success": True,

            "prediction": disease_name,

            "confidence": round(
                float(confidence),
                2
            ),

            "crop": info.get(
                "crop",
                "Unknown"
            ),

            "disease": info.get(
                "disease",
                disease_name
            ),

            "status": info.get(
                "status",
                "Unknown"
            ),

            "symptoms": info.get(
                "symptoms",
                "Information not available."
            ),

            "cause": info.get(
                "cause",
                "Information not available."
            ),

            "treatment": info.get(
                "treatment",
                "Information not available."
            ),

            "prevention": info.get(
                "prevention",
                "Information not available."
            )

        }


    except Exception as e:

        print("\n❌ PREDICTION ERROR:")
        print(str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )