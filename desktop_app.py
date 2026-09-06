import subprocess
import sys
import time
import webview
import urllib.request


# ==========================================
# START STREAMLIT
# ==========================================

streamlit_process = subprocess.Popen(
    [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "main.py",
        "--server.headless=true",
        "--browser.gatherUsageStats=false",
        "--server.address=127.0.0.1",
        "--server.port=8501"
    ],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)


# ==========================================
# WAIT FOR STREAMLIT
# ==========================================

url = "http://127.0.0.1:8501"

for _ in range(30):

    try:
        urllib.request.urlopen(url, timeout=1)
        break

    except Exception:
        time.sleep(1)

else:

    streamlit_process.terminate()

    raise RuntimeError(
        "Crop Care could not start the Streamlit server."
    )


# ==========================================
# OPEN CROP CARE DESKTOP WINDOW
# ==========================================

webview.create_window(
    "Crop Care 🌱",
    url,
    width=1200,
    height=800,
    resizable=True
)


# ==========================================
# START WINDOW
# ==========================================

webview.start()


# ==========================================
# CLOSE STREAMLIT WHEN APP CLOSES
# ==========================================

if streamlit_process.poll() is None:
    streamlit_process.terminate()