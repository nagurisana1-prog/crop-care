import streamlit as st
from utils.language import translations


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Crop Care",
    page_icon="🌱",
    layout="wide"
)


# ==========================================
# TERMS & CONDITIONS
# ==========================================

if "terms_accepted" not in st.session_state:
    st.session_state.terms_accepted = False


if not st.session_state.terms_accepted:

    st.markdown(
        """
        <style>

        .terms-title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            margin-top: 40px;
            margin-bottom: 10px;
        }

        .terms-subtitle {
            text-align: center;
            font-size: 20px;
            margin-bottom: 30px;
        }

        .terms-box {
            padding: 25px;
            border-radius: 15px;
            border: 1px solid #dddddd;
            margin-top: 20px;
            margin-bottom: 25px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="terms-title">🌱 Crop Care</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="terms-subtitle">Smart Crop Health Assistant</div>',
        unsafe_allow_html=True
    )

    # ------------------------------------------
    # LANGUAGE FOR TERMS PAGE
    # ------------------------------------------

    terms_language = st.selectbox(
        "🌐 Select Language / భాష ఎంచుకోండి / भाषा चुनें",
        ["English", "Telugu", "Hindi"],
        format_func=lambda x: {
            "English": "English",
            "Telugu": "తెలుగు",
            "Hindi": "हिन्दी"
        }[x]
    )

    # ------------------------------------------
    # TERMS CONTENT
    # ------------------------------------------

    if terms_language == "English":

        st.header("📜 Terms & Conditions")

        st.markdown(
            """
            <div class="terms-box">

            **Welcome to Crop Care! 🌱**

            Please read the following terms before using the application.

            **1. Purpose of the Application**

            Crop Care is an AI-based crop health assistance application
            designed to help users identify possible crop diseases from
            uploaded leaf images.

            **2. AI-Based Results**

            The results provided by Crop Care are generated using
            artificial intelligence and are intended for guidance and
            educational purposes. The results may not always be accurate.

            **3. No Guarantee**

            Crop Care does not guarantee that every disease, condition,
            or crop problem will be correctly identified.

            **4. Farmer Responsibility**

            Users should inspect their crops carefully and, when necessary,
            consult agricultural experts before taking major treatment
            or crop-management decisions.

            **5. Image Usage**

            Users should upload clear crop images and should avoid
            uploading personal, private, or sensitive information.

            **6. Limitation of Liability**

            Crop Care and its developers are not responsible for any
            loss, damage, crop failure, or financial loss resulting from
            decisions made solely on the basis of the application's results.

            **7. Acceptance**

            By selecting "I Agree & Continue", you confirm that you have
            read and understood these terms and agree to use Crop Care
            responsibly.

            </div>
            """,
            unsafe_allow_html=True
        )

        agree_text = "I Agree & Continue"

    elif terms_language == "Telugu":

        st.header("📜 నిబంధనలు మరియు షరతులు")

        st.markdown(
            """
            <div class="terms-box">

            **Crop Care కు స్వాగతం! 🌱**

            ఈ అప్లికేషన్‌ను ఉపయోగించే ముందు క్రింది నిబంధనలు చదవండి.

            **1. అప్లికేషన్ యొక్క ఉద్దేశ్యం**

            Crop Care అనేది కృత్రిమ మేధస్సును ఉపయోగించి పంట ఆకుల
            చిత్రాల ఆధారంగా పంట వ్యాధులను గుర్తించడంలో సహాయపడే అప్లికేషన్.

            **2. AI ఫలితాలు**

            Crop Care అందించే ఫలితాలు కృత్రిమ మేధస్సు ఆధారంగా ఉంటాయి.
            ఇవి మార్గదర్శకత్వం మరియు విద్యా ప్రయోజనాల కోసం మాత్రమే.
            ఫలితాలు ఎల్లప్పుడూ ఖచ్చితంగా ఉండకపోవచ్చు.

            **3. హామీ లేదు**

            ప్రతి వ్యాధిని లేదా పంట సమస్యను Crop Care ఖచ్చితంగా
            గుర్తిస్తుందని హామీ ఇవ్వలేము.

            **4. రైతు బాధ్యత**

            వినియోగదారులు తమ పంటలను జాగ్రత్తగా పరిశీలించాలి.
            అవసరమైనప్పుడు వ్యవసాయ నిపుణుల సలహా తీసుకోవాలి.

            **5. చిత్రాల వినియోగం**

            స్పష్టమైన పంట చిత్రాలను మాత్రమే అప్‌లోడ్ చేయండి.
            వ్యక్తిగత లేదా సున్నితమైన సమాచారాన్ని అప్‌లోడ్ చేయవద్దు.

            **6. బాధ్యత పరిమితి**

            అప్లికేషన్ ఫలితాల ఆధారంగా తీసుకున్న నిర్ణయాల వల్ల కలిగే
            పంట నష్టం లేదా ఆర్థిక నష్టాలకు Crop Care మరియు దాని
            అభివృద్ధిదారులు బాధ్యత వహించరు.

            **7. అంగీకారం**

            "అంగీకరించి కొనసాగించండి" ఎంచుకోవడం ద్వారా మీరు ఈ
            నిబంధనలను చదివి అర్థం చేసుకున్నారని మరియు Crop Care ను
            బాధ్యతాయుతంగా ఉపయోగించడానికి అంగీకరిస్తున్నారని నిర్ధారిస్తారు.

            </div>
            """,
            unsafe_allow_html=True
        )

        agree_text = "అంగీకరించి కొనసాగించండి"

    else:

        st.header("📜 नियम और शर्तें")

        st.markdown(
            """
            <div class="terms-box">

            **Crop Care में आपका स्वागत है! 🌱**

            एप्लिकेशन का उपयोग करने से पहले कृपया निम्नलिखित नियम पढ़ें।

            **1. एप्लिकेशन का उद्देश्य**

            Crop Care एक AI आधारित एप्लिकेशन है जो पत्तियों की तस्वीरों
            के आधार पर संभावित फसल रोगों की पहचान करने में सहायता करता है।

            **2. AI परिणाम**

            Crop Care द्वारा दिए गए परिणाम कृत्रिम बुद्धिमत्ता पर आधारित हैं
            और केवल मार्गदर्शन एवं शैक्षणिक उद्देश्यों के लिए हैं।
            परिणाम हमेशा पूरी तरह सटीक नहीं हो सकते।

            **3. कोई गारंटी नहीं**

            Crop Care हर बीमारी या फसल की समस्या की सही पहचान की
            गारंटी नहीं देता।

            **4. किसान की जिम्मेदारी**

            उपयोगकर्ताओं को अपनी फसलों की सावधानीपूर्वक जांच करनी चाहिए
            और आवश्यकता पड़ने पर कृषि विशेषज्ञों की सलाह लेनी चाहिए।

            **5. तस्वीरों का उपयोग**

            कृपया साफ फसल की तस्वीरें अपलोड करें और व्यक्तिगत या
            संवेदनशील जानकारी अपलोड न करें।

            **6. जिम्मेदारी की सीमा**

            एप्लिकेशन के परिणामों के आधार पर लिए गए निर्णयों से होने वाले
            फसल नुकसान या आर्थिक नुकसान के लिए Crop Care और उसके
            डेवलपर्स जिम्मेदार नहीं होंगे।

            **7. स्वीकृति**

            "सहमत होकर जारी रखें" चुनकर आप पुष्टि करते हैं कि आपने
            इन नियमों को पढ़ और समझ लिया है तथा Crop Care का
            जिम्मेदारी से उपयोग करने के लिए सहमत हैं।

            </div>
            """,
            unsafe_allow_html=True
        )

        agree_text = "सहमत होकर जारी रखें"

    # ------------------------------------------
    # AGREEMENT
    # ------------------------------------------

    st.warning(
        "⚠️ Please read and understand the Terms & Conditions before continuing."
        if terms_language == "English"
        else
        "⚠️ కొనసాగించే ముందు నిబంధనలు మరియు షరతులను చదివి అర్థం చేసుకోండి."
        if terms_language == "Telugu"
        else
        "⚠️ आगे बढ़ने से पहले नियम और शर्तों को पढ़ें और समझें।"
    )

    if st.button(
        agree_text,
        use_container_width=True,
        type="primary"
    ):

        st.session_state.terms_accepted = True
        st.session_state.language = terms_language

        st.rerun()

    st.stop()


# ==========================================
# LANGUAGE
# ==========================================

if "language" not in st.session_state:
    st.session_state.language = "English"


language_names = {
    "English": "English",
    "Telugu": "తెలుగు",
    "Hindi": "हिन्दी"
}


selected_language = st.selectbox(
    "🌐 Language / భాష / भाषा",
    list(language_names.keys()),
    format_func=lambda x: language_names[x],
    index=list(language_names.keys()).index(
        st.session_state.language
    )
)


st.session_state.language = selected_language

t = translations[selected_language]


# ==========================================
# CUSTOM STYLE
# ==========================================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 30px;
    }

    .feature-box {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #dddddd;
        margin-bottom: 10px;
        min-height: 100px;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        padding: 20px;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# HEADER
# ==========================================

st.markdown(
    f'<div class="main-title">🌱 Crop Care</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="subtitle">{t["welcome"]}</div>',
    unsafe_allow_html=True
)


# ==========================================
# INTRODUCTION
# ==========================================

st.info(t["intro"])

st.divider()


# ==========================================
# START DETECTION
# ==========================================

st.header(t["start"])

st.write(
    "📷 "
    + (
        "Take a picture or upload a crop leaf image "
        "to begin disease detection."
        if selected_language == "English"
        else
        "వ్యాధి గుర్తింపు ప్రారంభించడానికి పంట ఆకు ఫోటో తీయండి లేదా చిత్రాన్ని అప్‌లోడ్ చేయండి."
        if selected_language == "Telugu"
        else
        "रोग पहचान शुरू करने के लिए फसल की पत्ती की तस्वीर लें या अपलोड करें।"
    )
)


if st.button(
    t["start"],
    use_container_width=True
):

    st.switch_page("pages/detection.py")


st.divider()


# ==========================================
# FEATURES
# ==========================================

st.header(t["features"])


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        f"""
        <div class="feature-box">
        <h3>🌱</h3>
        <b>{t["feature1"]}</b>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="feature-box">
        <h3>🤖</h3>
        <b>{t["feature2"]}</b>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="feature-box">
        <h3>📷</h3>
        <b>{t["feature3"]}</b>
        </div>
        """,
        unsafe_allow_html=True
    )


col4, col5 = st.columns(2)


with col4:

    st.markdown(
        f"""
        <div class="feature-box">
        <h3>📖</h3>
        <b>{t["feature4"]}</b>
        </div>
        """,
        unsafe_allow_html=True
    )


with col5:

    st.markdown(
        f"""
        <div class="feature-box">
        <h3>🌐</h3>
        <b>{t["feature5"]}</b>
        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ==========================================
# HOW IT WORKS
# ==========================================

st.header(t["how_it_works"])

st.write(t["step1"])
st.write(t["step2"])
st.write(t["step3"])
st.write(t["step4"])


st.divider()


# ==========================================
# ABOUT
# ==========================================

st.header(t["about"])

st.write(t["about_text"])


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <div class="footer">
    🌱 Crop Care
    <br>
    🤖 Powered by Artificial Intelligence
    </div>
    """,
    unsafe_allow_html=True
)