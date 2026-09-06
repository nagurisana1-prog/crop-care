import PyInstaller.__main__

PyInstaller.__main__.run([
    "desktop_app.py",

    "--name=CropCare",

    "--windowed",

    "--onedir",

    "--clean",

    "--add-data=main.py;.",
    "--add-data=pages;pages",
    "--add-data=utils;utils",
    "--add-data=model;model",
    "--add-data=disease_info.json;.",

    "--collect-all=streamlit",
    "--collect-all=watchdog",
    "--collect-all=altair",
    "--collect-all=pydeck",
])