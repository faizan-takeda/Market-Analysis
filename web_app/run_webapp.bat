@echo off
setlocal
cd /d "%~dp0"
title MEDICINE 2040 web app

where node >nul 2>nul
if errorlevel 1 (
  echo Node.js 18 or newer is required. Install the LTS version from https://nodejs.org and run this file again.
  pause
  exit /b 1
)

if not exist node_modules (
  echo Installing dependencies - one time, needs internet...
  call npm install --no-audit --no-fund
  if errorlevel 1 ( echo npm install failed. & pause & exit /b 1 )
)

if not exist dist\index.html (
  echo Building the app...
  call npm run build
  if errorlevel 1 ( echo build failed. & pause & exit /b 1 )
)

echo.
echo MEDICINE 2040 web app  -  http://127.0.0.1:4173/
echo Close this window to stop the server.
echo.
start "" /b cmd /c "timeout /t 3 >nul & start http://127.0.0.1:4173/"
call npm run preview
pause
