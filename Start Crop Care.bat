@echo off
title Crop Care

echo ========================================
echo          CROP CARE - AI
echo ========================================
echo.

cd /d "C:\Users\sanan\Desktop\AI_Crop_Disease_Detection"

echo [1/2] Starting AI Server...
start "Crop Care - AI Server" cmd /k "python -m uvicorn backend:app --host 0.0.0.0 --port 8000"

timeout /t 3 /nobreak >nul

echo [2/2] Starting Crop Care Web...
cd /d "C:\Users\sanan\Desktop\AI_Crop_Disease_Detection\frontend"

start "Crop Care - Web" cmd /k "npm run dev -- --host 0.0.0.0"

timeout /t 5 /nobreak >nul

start "" "http://localhost:5173"

echo.
echo Crop Care is starting...
echo.
pause