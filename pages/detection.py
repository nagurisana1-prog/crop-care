import streamlit as st
from PIL import Image
import os
import json

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Crop Care",
    page_icon="🌱",
    layout="centered"
)

# --------------------------------------------------
# LOAD DISEASE INFORMATION
# --------------------------------------------------

DISEASE_INFO_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "disease_info.json"
)

disease_info = {}

if os.path.exists(DISEASE_INFO_PATH):
    try:
        with open(DISEASE_INFO_PATH, "r", encoding="utf-8") as file:
            disease_info = json.load(file)
    except Exception:
        disease_info = {}

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🌱 AI Crop Disease Detection")
st.write("Upload a crop leaf image and let the AI analyze it.")

st.divider()

# --------------------------------------------------
# IMAGE INPUT
# --------------------------------------------------
st.subheader("📷 Upload Leaf Image")

uploaded_file = st.file_uploader(
    "Choose an image of a crop leaf",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Leaf",
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------
    # DETECTION BUTTON
    # --------------------------------------------------

    if st.button("🔍 Detect Disease", use_container_width=True):

        with st.spinner("🤖 Analyzing the leaf..."):

            try:

                # Try loading the prediction function
                from utils.predictor import predict_disease

                result = predict_disease(image)

                # --------------------------------------------------
                # HANDLE DIFFERENT RESULT FORMATS
                # --------------------------------------------------

                if isinstance(result, tuple):

                    disease_name = result[0]

                    confidence = (
                        result[1]
                        if len(result) > 1
                        else None
                    )

                else:

                    disease_name = result
                    confidence = None

                # --------------------------------------------------
                # RESULT
                # --------------------------------------------------

                st.success("✅ Analysis Complete")

                st.subheader("🌿 Detection Result")

                st.markdown(
                    f"### {disease_name}"
                )

                if confidence is not None:

                    try:

                        confidence_value = float(confidence)

                        if confidence_value <= 1:
                            confidence_value *= 100

                        st.metric(
                            "Confidence",
                            f"{confidence_value:.2f}%"
                        )

                    except Exception:
                        pass

                # --------------------------------------------------
                # DISEASE INFORMATION
                # --------------------------------------------------

                info = disease_info.get(disease_name)

                if info:

                    st.divider()

                    st.subheader("📋 About the Disease")

                    if isinstance(info, dict):

                        if "description" in info:
                            st.write(
                                info["description"]
                            )

                        if "symptoms" in info:

                            st.markdown("**🔎 Symptoms**")

                            symptoms = info["symptoms"]

                            if isinstance(symptoms, list):

                                for symptom in symptoms:
                                    st.write(f"• {symptom}")

                            else:
                                st.write(symptoms)

                        if "treatment" in info:

                            st.markdown("**💊 Treatment**")

                            st.write(info["treatment"])

                        if "prevention" in info:

                            st.markdown("**🛡️ Prevention**")

                            st.write(info["prevention"])

                    else:

                        st.write(info)

                # --------------------------------------------------
                # FARMER ADVICE
                # --------------------------------------------------

                st.divider()

                st.subheader("🌾 What You Can Do")

                # Use information from disease_info.json

                if info and isinstance(info, dict):

                    status = str(
                        info.get("status", "")
                    ).lower()

                    if status == "healthy":

                        st.success(
                            "🌱 Your plant appears healthy!"
                        )

                        st.write(
                            "💧 **Care:** "
                            + info.get(
                                "prevention",
                                "Continue proper crop care and regular monitoring."
                            )
                        )

                    else:

                        st.warning(
                            "⚠️ The plant may need attention."
                        )

                        st.markdown(
                            "🩺 **What to do:** "
                            + info.get(
                                "treatment",
                                "Follow suitable crop disease management practices."
                            )
                        )

                        st.markdown(
                            "🛡️ **How to prevent it:** "
                            + info.get(
                                "prevention",
                                "Monitor the crop regularly."
                            )
                        )

                # --------------------------------------------------
                # FALLBACK IF DISEASE INFORMATION IS NOT FOUND
                # --------------------------------------------------

                else:

                    if "healthy" in str(
                        disease_name
                    ).lower():

                        st.success(
                            "🌱 Your plant appears healthy! "
                            "Continue proper watering, sunlight, "
                            "nutrition and regular monitoring."
                        )

                    else:

                        st.warning(
                            "⚠️ Disease detected. "
                            "Please inspect the plant and follow "
                            "appropriate crop management practices."
                        )

            except ImportError:

                st.error(
                    "❌ The prediction module is not connected yet."
                )

                st.info(
                    "Your detection page is ready, but "
                    "`utils/predictor.py` needs to be connected "
                    "to the trained AI model."
                )

            except Exception as e:

                st.error(
                    "❌ Something went wrong while analyzing the image."
                )

                st.code(str(e))

else:

    st.info(
        "📷 Upload a clear image of a crop leaf to begin detection."
    )

# --------------------------------------------------
# BACK BUTTON
# --------------------------------------------------

st.divider()

if st.button("⬅️ Back to Home", use_container_width=True):

    st.switch_page("main.py")