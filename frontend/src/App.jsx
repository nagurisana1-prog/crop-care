import { useState, useRef, useEffect } from "react";
import "./App.css";

const translations = {
  English: {
    home: "Home",
    detect: "Detect Disease",
    about: "About",
    tagline: "SMART FARMING WITH AI",
    heroTitle1: "Protect Your Crops",
    heroTitle2: "With Artificial Intelligence",
    heroDescription:
      "Upload a photo of your crop leaf and let Crop Care identify possible diseases and provide useful information for treatment and prevention.",
    detectButton: "🔍 Detect Disease",
    aiPowered: "AI POWERED DETECTION",
    checkCrop: "Check Your Crop",
    uploadInstruction:
      "Upload a clear image of the crop leaf to begin.",
    uploadTitle: "Upload Leaf Image",
    uploadDescription:
      "Click here to choose a JPG, JPEG or PNG image",
    changeImage: "📷 Change Image",
    analyzing: "🤖 Analyzing...",
    analysisComplete: "🌱 AI ANALYSIS COMPLETE",
    healthy: "🌿 Healthy",
    diseased: "⚠️ Diseased",
    confidence: "AI Confidence",
    crop: "🌾 Crop",
    symptoms: "🔎 Symptoms",
    cause: "🦠 Cause",
    treatment: "💊 Treatment",
    prevention: "🛡️ Prevention",
    whatYouCanDo: "🌱 What You Can Do",
    healthyAdvice:
      "Your plant appears healthy! Continue proper watering, sunlight, nutrition and regular monitoring.",
    diseasedAdvice:
      "Your plant may need attention. Follow the recommended treatment and prevention steps, and monitor the plant regularly.",
    aboutLabel: "ABOUT CROP CARE",
    aboutTitle1: "Making Crop Health",
    aboutTitle2: "Smarter With AI",
    aboutDescription:
      "Crop Care uses an AI-powered image classification model to analyze crop leaves and identify common plant diseases. It provides farmers with simple, understandable information about symptoms, causes, treatment and prevention.",
    footer: "AI-powered crop health assistance 🌾",
    uploadFirst: "Please upload a crop leaf image first.",
    connectionError:
      "Unable to connect to the AI server. Make sure FastAPI is running.",
    takePhoto: "📷 Take Photo",
    chooseImage: "📁 Choose Image",
    capturePhoto: "📸 Capture Photo",
    cancel: "❌ Cancel",
    cameraError:
      "❌ Camera access was denied or is not available. Please allow camera permission in your browser.",
    cameraNotReady:
      "❌ Camera is not ready yet. Please wait a moment.",
    captureError:
      "❌ Unable to capture the photo.",
  },

  Telugu: {
    home: "హోమ్",
    detect: "వ్యాధిని గుర్తించండి",
    about: "మా గురించి",
    tagline: "AI తో స్మార్ట్ వ్యవసాయం",
    heroTitle1: "మీ పంటలను రక్షించండి",
    heroTitle2: "కృత్రిమ మేధస్సుతో",
    heroDescription:
      "మీ పంట ఆకుకు సంబంధించిన ఫోటోను అప్‌లోడ్ చేయండి. Crop Care సాధ్యమైన వ్యాధులను గుర్తించి చికిత్స మరియు నివారణకు ఉపయోగకరమైన సమాచారాన్ని అందిస్తుంది.",
    detectButton: "🔍 వ్యాధిని గుర్తించండి",
    aiPowered: "AI ఆధారిత గుర్తింపు",
    checkCrop: "మీ పంటను తనిఖీ చేయండి",
    uploadInstruction:
      "ప్రారంభించడానికి పంట ఆకు యొక్క స్పష్టమైన చిత్రాన్ని అప్‌లోడ్ చేయండి.",
    uploadTitle: "ఆకు చిత్రాన్ని అప్‌లోడ్ చేయండి",
    uploadDescription:
      "JPG, JPEG లేదా PNG చిత్రాన్ని ఎంచుకోవడానికి ఇక్కడ క్లిక్ చేయండి",
    changeImage: "📷 చిత్రాన్ని మార్చండి",
    analyzing: "🤖 విశ్లేషిస్తోంది...",
    analysisComplete: "🌱 AI విశ్లేషణ పూర్తయింది",
    healthy: "🌿 ఆరోగ్యకరమైనది",
    diseased: "⚠️ వ్యాధి గుర్తించబడింది",
    confidence: "AI నమ్మక స్థాయి",
    crop: "🌾 పంట",
    symptoms: "🔎 లక్షణాలు",
    cause: "🦠 కారణం",
    treatment: "💊 చికిత్స",
    prevention: "🛡️ నివారణ",
    whatYouCanDo: "🌱 మీరు చేయగలిగేది",
    healthyAdvice:
      "మీ మొక్క ఆరోగ్యంగా కనిపిస్తోంది! సరైన నీరు, సూర్యకాంతి, పోషకాలు అందిస్తూ క్రమం తప్పకుండా పర్యవేక్షించండి.",
    diseasedAdvice:
      "మీ మొక్కకు శ్రద్ధ అవసరం కావచ్చు. సూచించిన చికిత్స మరియు నివారణ చర్యలను పాటిస్తూ మొక్కను క్రమం తప్పకుండా పర్యవేక్షించండి.",
    aboutLabel: "CROP CARE గురించి",
    aboutTitle1: "AI తో పంట ఆరోగ్యాన్ని",
    aboutTitle2: "మరింత స్మార్ట్‌గా",
    aboutDescription:
      "Crop Care AI ఆధారిత ఇమేజ్ క్లాసిఫికేషన్ మోడల్‌ను ఉపయోగించి పంట ఆకులను విశ్లేషిస్తుంది మరియు సాధారణ మొక్కల వ్యాధులను గుర్తిస్తుంది. ఇది లక్షణాలు, కారణాలు, చికిత్స మరియు నివారణ గురించి రైతులకు సులభమైన సమాచారాన్ని అందిస్తుంది.",
    footer: "AI ఆధారిత పంట ఆరోగ్య సహాయం 🌾",
    uploadFirst: "ముందుగా పంట ఆకు చిత్రాన్ని అప్‌లోడ్ చేయండి.",
    connectionError:
      "AI సర్వర్‌కు కనెక్ట్ కాలేకపోయింది. FastAPI నడుస్తుందో లేదో తనిఖీ చేయండి.",
    takePhoto: "📷 ఫోటో తీయండి",
    chooseImage: "📁 చిత్రాన్ని ఎంచుకోండి",
    capturePhoto: "📸 ఫోటో క్యాప్చర్ చేయండి",
    cancel: "❌ రద్దు చేయండి",
    cameraError:
      "❌ కెమెరా యాక్సెస్ తిరస్కరించబడింది లేదా అందుబాటులో లేదు. దయచేసి బ్రౌజర్‌లో కెమెరా అనుమతిని ఇవ్వండి.",
    cameraNotReady:
      "❌ కెమెరా ఇంకా సిద్ధంగా లేదు. దయచేసి కొద్దిసేపు వేచి ఉండండి.",
    captureError:
      "❌ ఫోటోను క్యాప్చర్ చేయలేకపోయాము.",
  },

  Hindi: {
    home: "होम",
    detect: "रोग पहचानें",
    about: "हमारे बारे में",
    tagline: "AI के साथ स्मार्ट खेती",
    heroTitle1: "अपनी फसलों की रक्षा करें",
    heroTitle2: "कृत्रिम बुद्धिमत्ता के साथ",
    heroDescription:
      "अपनी फसल के पत्ते की तस्वीर अपलोड करें। Crop Care संभावित रोगों की पहचान करेगा और उपचार एवं रोकथाम के लिए उपयोगी जानकारी देगा।",
    detectButton: "🔍 रोग पहचानें",
    aiPowered: "AI आधारित पहचान",
    checkCrop: "अपनी फसल की जाँच करें",
    uploadInstruction:
      "शुरू करने के लिए फसल के पत्ते की साफ तस्वीर अपलोड करें।",
    uploadTitle: "पत्ते की तस्वीर अपलोड करें",
    uploadDescription:
      "JPG, JPEG या PNG तस्वीर चुनने के लिए यहाँ क्लिक करें",
    changeImage: "📷 तस्वीर बदलें",
    analyzing: "🤖 विश्लेषण हो रहा है...",
    analysisComplete: "🌱 AI विश्लेषण पूरा हुआ",
    healthy: "🌿 स्वस्थ",
    diseased: "⚠️ रोगग्रस्त",
    confidence: "AI का विश्वास स्तर",
    crop: "🌾 फसल",
    symptoms: "🔎 लक्षण",
    cause: "🦠 कारण",
    treatment: "💊 उपचार",
    prevention: "🛡️ रोकथाम",
    whatYouCanDo: "🌱 आप क्या कर सकते हैं",
    healthyAdvice:
      "आपका पौधा स्वस्थ दिखाई देता है! उचित पानी, धूप और पोषण देते रहें तथा नियमित रूप से पौधे की निगरानी करें।",
    diseasedAdvice:
      "आपके पौधे को ध्यान देने की आवश्यकता हो सकती है। सुझाए गए उपचार और रोकथाम के उपायों का पालन करें और पौधे की नियमित निगरानी करें।",
    aboutLabel: "CROP CARE के बारे में",
    aboutTitle1: "AI के साथ फसल स्वास्थ्य को",
    aboutTitle2: "और बेहतर बनाना",
    aboutDescription:
      "Crop Care AI आधारित इमेज क्लासिफिकेशन मॉडल का उपयोग करके फसल के पत्तों का विश्लेषण करता है और सामान्य पौधों के रोगों की पहचान करता है। यह किसानों को लक्षण, कारण, उपचार और रोकथाम के बारे में सरल जानकारी देता है।",
    footer: "AI आधारित फसल स्वास्थ्य सहायता 🌾",
    uploadFirst: "कृपया पहले फसल के पत्ते की तस्वीर अपलोड करें।",
    connectionError:
      "AI सर्वर से कनेक्ट नहीं हो पाया। सुनिश्चित करें कि FastAPI चल रहा है।",
    takePhoto: "📷 फोटो लें",
    chooseImage: "📁 तस्वीर चुनें",
    capturePhoto: "📸 फोटो कैप्चर करें",
    cancel: "❌ रद्द करें",
    cameraError:
      "❌ कैमरा एक्सेस अस्वीकार कर दिया गया या उपलब्ध नहीं है। कृपया ब्राउज़र में कैमरा अनुमति दें।",
    cameraNotReady:
      "❌ कैमरा अभी तैयार नहीं है। कृपया कुछ देर प्रतीक्षा करें।",
    captureError:
      "❌ फोटो कैप्चर नहीं हो सकी।",
  },
};


function App() {

  const [language, setLanguage] = useState("English");

  const [selectedFile, setSelectedFile] = useState(null);

  const [preview, setPreview] = useState(null);

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const [cameraOpen, setCameraOpen] = useState(false);

  const [videoStream, setVideoStream] = useState(null);

  const videoRef = useRef(null);

  const t = translations[language];


  // ==========================================
  // START CAMERA
  // ==========================================

  const startCamera = async () => {

    try {

      setError("");

      if (
        !navigator.mediaDevices ||
        !navigator.mediaDevices.getUserMedia
      ) {

        setError(
          "❌ Your browser does not support camera access."
        );

        return;
      }

      const stream =
        await navigator.mediaDevices.getUserMedia({
          video: true,
          audio: false,
        });

      setVideoStream(stream);

      setCameraOpen(true);

    } catch (err) {

      console.error(err);

      setError(t.cameraError);
    }
  };


  // ==========================================
  // CONNECT CAMERA TO VIDEO
  // ==========================================

  useEffect(() => {

    if (
      videoRef.current &&
      videoStream
    ) {

      videoRef.current.srcObject =
        videoStream;

      videoRef.current
        .play()
        .catch(() => { });

    }

  }, [videoStream]);


  // ==========================================
  // STOP CAMERA
  // ==========================================

  const stopCamera = () => {

    if (videoStream) {

      videoStream
        .getTracks()
        .forEach((track) => {
          track.stop();
        });
    }

    setVideoStream(null);

    setCameraOpen(false);
  };


  // ==========================================
  // CAPTURE PHOTO
  // ==========================================

  const capturePhoto = () => {

    const video = videoRef.current;

    if (
      !video ||
      video.videoWidth === 0 ||
      video.videoHeight === 0
    ) {

      setError(t.cameraNotReady);

      return;
    }

    const canvas =
      document.createElement("canvas");

    canvas.width =
      video.videoWidth;

    canvas.height =
      video.videoHeight;

    const context =
      canvas.getContext("2d");

    context.drawImage(
      video,
      0,
      0,
      canvas.width,
      canvas.height
    );

    canvas.toBlob(
      (blob) => {

        if (!blob) {

          setError(t.captureError);

          return;
        }

        const file = new File(
          [blob],
          "crop-camera-photo.jpg",
          {
            type: "image/jpeg",
          }
        );

        setSelectedFile(file);

        setPreview(
          URL.createObjectURL(blob)
        );

        setResult(null);

        setError("");

        stopCamera();
      },
      "image/jpeg"
    );
  };


  // ==========================================
  // FILE UPLOAD
  // ==========================================

  const handleFileChange = (event) => {

    const file =
      event.target.files[0];

    if (!file) return;

    setSelectedFile(file);

    setPreview(
      URL.createObjectURL(file)
    );

    setResult(null);

    setError("");
  };


  // ==========================================
  // DETECT DISEASE
  // ==========================================

  const detectDisease = async () => {

    if (!selectedFile) {

      setError(t.uploadFirst);

      return;
    }

    setLoading(true);

    setError("");

    setResult(null);

    try {

      const formData =
        new FormData();

      formData.append(
        "file",
        selectedFile
      );

      const response =
        await fetch(
          "http://192.168.1.10:8000/predict",
          {
            method: "POST",
            body: formData,
          }
        );

      const data =
        await response.json();

      if (!data.success) {

        throw new Error(
          data.error ||
          "Prediction failed."
        );
      }

      setResult(data);

    } catch (err) {

      console.error(err);

      setError(
        t.connectionError
      );

    } finally {

      setLoading(false);
    }
  };


  return (

    <div className="app">


      {/* ==========================================
          HEADER
      ========================================== */}

      <header className="header">

        <div className="logo">

          🌱 <span>Crop Care</span>

        </div>


        <nav>

          <a href="#home">
            {t.home}
          </a>

          <a href="#detect">
            {t.detect}
          </a>

          <a href="#about">
            {t.about}
          </a>


          <select
            value={language}
            onChange={(e) =>
              setLanguage(e.target.value)
            }
          >

            <option value="English">
              🇬🇧 English
            </option>

            <option value="Telugu">
              🇮🇳 తెలుగు
            </option>

            <option value="Hindi">
              🇮🇳 हिन्दी
            </option>

          </select>

        </nav>

      </header>


      {/* ==========================================
          HERO
      ========================================== */}

      <section
        className="hero"
        id="home"
      >

        <div className="hero-text">

          <p className="tagline">
            🌾 {t.tagline}
          </p>

          <h1>

            {t.heroTitle1}

            <br />

            <span>
              {t.heroTitle2}
            </span>

          </h1>


          <p className="hero-description">

            {t.heroDescription}

          </p>


          <a
            href="#detect"
            className="hero-button"
          >

            {t.detectButton}

          </a>

        </div>


        <div className="hero-icon">

          🌿

        </div>

      </section>


      {/* ==========================================
          DETECTION
      ========================================== */}

      <section
        className="detection-section"
        id="detect"
      >

        <div className="section-heading">

          <p>
            {t.aiPowered}
          </p>

          <h2>
            {t.checkCrop}
          </h2>

          <span>
            {t.uploadInstruction}
          </span>

        </div>


        <div className="upload-card">


          {/* ==========================================
              UPLOAD / CAMERA
          ========================================== */}

          {!preview ? (

            <div className="upload-area">

              <div className="upload-icon">
                🌿
              </div>

              <h3>
                {t.uploadTitle}
              </h3>

              <p>
                {t.uploadDescription}
              </p>


              <div className="upload-buttons">


                {/* CAMERA */}

                <button
                  type="button"
                  className="camera-button"
                  onClick={startCamera}
                >

                  {t.takePhoto}

                </button>


                {/* GALLERY */}

                <label className="gallery-button">

                  {t.chooseImage}

                  <input
                    type="file"
                    accept="image/png,image/jpeg,image/jpg"
                    onChange={handleFileChange}
                    hidden
                  />

                </label>

              </div>


              {/* CAMERA VIEW */}

              {cameraOpen && (

                <div className="camera-container">

                  <video
                    ref={videoRef}
                    className="camera-preview"
                    autoPlay
                    playsInline
                  />


                  <div className="camera-controls">

                    <button
                      type="button"
                      onClick={capturePhoto}
                      className="capture-button"
                    >

                      {t.capturePhoto}

                    </button>


                    <button
                      type="button"
                      onClick={stopCamera}
                      className="cancel-camera-button"
                    >

                      {t.cancel}

                    </button>

                  </div>

                </div>

              )}

            </div>

          ) : (

            <div className="preview-area">

              <img
                src={preview}
                alt="Uploaded crop leaf"
              />


              <button
                type="button"
                className="camera-button"
                onClick={startCamera}
              >

                {t.takePhoto}

              </button>


              {cameraOpen && (

                <div className="camera-container">

                  <video
                    ref={videoRef}
                    className="camera-preview"
                    autoPlay
                    playsInline
                  />


                  <div className="camera-controls">

                    <button
                      type="button"
                      onClick={capturePhoto}
                      className="capture-button"
                    >

                      {t.capturePhoto}

                    </button>


                    <button
                      type="button"
                      onClick={stopCamera}
                      className="cancel-camera-button"
                    >

                      {t.cancel}

                    </button>

                  </div>

                </div>

              )}

            </div>

          )}


          {/* ==========================================
              DETECT BUTTON
          ========================================== */}

          {selectedFile && (

            <button
              className="detect-button"
              onClick={detectDisease}
              disabled={loading}
            >

              {loading
                ? t.analyzing
                : t.detectButton}

            </button>

          )}


          {/* ==========================================
              ERROR
          ========================================== */}

          {error && (

            <div className="error-message">

              ⚠️ {error}

            </div>

          )}

        </div>


        {/* ==========================================
            RESULT
        ========================================== */}

        {result && (

          <div className="result-card">


            {/* RESULT HEADER */}

            <div className="result-header">

              <p>
                {t.analysisComplete}
              </p>

              <h2>
                {result.disease}
              </h2>

              <span
                className={
                  result.status === "Healthy"
                    ? "status healthy"
                    : "status diseased"
                }
              >

                {result.status === "Healthy"
                  ? t.healthy
                  : t.diseased}

              </span>

            </div>


            {/* ==========================================
                CONFIDENCE
            ========================================== */}

            <div className="confidence">

              <div className="confidence-top">

                <span>
                  {t.confidence}
                </span>

                <strong>

                  {result.confidence <= 1
                    ? (
                      result.confidence * 100
                    ).toFixed(2)
                    : result.confidence.toFixed(2)}

                  %

                </strong>

              </div>


              <div className="progress-bar">

                <div
                  className="progress"
                  style={{
                    width: `${result.confidence <= 1
                      ? result.confidence * 100
                      : result.confidence
                      }%`,
                  }}
                />

              </div>

            </div>


            {/* ==========================================
                INFORMATION
            ========================================== */}

            <div className="info-grid">


              <div className="info-box">

                <h3>
                  {t.crop}
                </h3>

                <p>
                  {result.crop}
                </p>

              </div>


              <div className="info-box">

                <h3>
                  {t.symptoms}
                </h3>

                <p>
                  {result.symptoms}
                </p>

              </div>


              <div className="info-box">

                <h3>
                  {t.cause}
                </h3>

                <p>
                  {result.cause}
                </p>

              </div>


              <div className="info-box">

                <h3>
                  {t.treatment}
                </h3>

                <p>
                  {result.treatment}
                </p>

              </div>


              <div className="info-box">

                <h3>
                  {t.prevention}
                </h3>

                <p>
                  {result.prevention}
                </p>

              </div>


            </div>


            {/* ==========================================
                WHAT YOU CAN DO
            ========================================== */}

            <div
              className={
                result.status === "Healthy"
                  ? "farmer-advice healthy-advice"
                  : "farmer-advice"
              }
            >

              <h3>
                {t.whatYouCanDo}
              </h3>


              {result.status === "Healthy" ? (

                <>

                  <p>
                    {t.healthyAdvice}
                  </p>


                  {result.prevention && (

                    <>

                      <h4>
                        🛡️ {t.prevention}
                      </h4>

                      <p>
                        {result.prevention}
                      </p>

                    </>

                  )}

                </>

              ) : (

                <>

                  <p>
                    {t.diseasedAdvice}
                  </p>


                  {result.treatment && (

                    <>

                      <h4>
                        {t.treatment}
                      </h4>

                      <p>
                        {result.treatment}
                      </p>

                    </>

                  )}


                  {result.prevention && (

                    <>

                      <h4>
                        {t.prevention}
                      </h4>

                      <p>
                        {result.prevention}
                      </p>

                    </>

                  )}

                </>

              )}

            </div>


          </div>

        )}

      </section>


      {/* ==========================================
          ABOUT
      ========================================== */}

      <section
        className="about-section"
        id="about"
      >

        <p className="about-label">
          {t.aboutLabel}
        </p>


        <h2>

          {t.aboutTitle1}

          <br />

          <span>
            {t.aboutTitle2}
          </span>

        </h2>


        <p>
          {t.aboutDescription}
        </p>

      </section>


      {/* ==========================================
          FOOTER
      ========================================== */}

      <footer>

        <div className="logo">

          🌱 <span>Crop Care</span>

        </div>

        <p>
          {t.footer}
        </p>

      </footer>


    </div>
  );
}

export default App;