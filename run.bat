@echo off
REM BalanceBuddy AI launcher (Windows)
setlocal

cd /d "%~dp0"

REM Activate venv if exists
if exist ".venv\Scripts\activate.bat" (
  call ".venv\Scripts\activate.bat"
)

REM Check Python
where python >nul 2>nul
if errorlevel 1 (
  echo [X] Python chua duoc cai. Cai Python 3.10+ tu https://python.org roi chay lai.
  pause
  exit /b 1
)

REM Check requirements
python -c "import fastapi" 2>nul
if errorlevel 1 (
  echo [!] Chua cai requirements. Dang cai...
  python -m pip install -r requirements.txt
  if errorlevel 1 (
    echo [X] Loi cai requirements. Kiem tra ket noi internet.
    pause
    exit /b 1
  )
)

REM Run from backend/
cd backend
echo.
echo [*] Khoi dong BalanceBuddy AI tai http://localhost:8000 ...
echo.
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

endlocal
