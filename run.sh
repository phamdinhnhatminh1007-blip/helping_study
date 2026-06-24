#!/usr/bin/env bash
# BalanceBuddy AI launcher (macOS / Linux)
set -euo pipefail

cd "$(dirname "$0")"

# Activate venv if it exists
if [ -d ".venv" ]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

# Check Python
if ! command -v python3 &> /dev/null; then
  echo "❌ Python 3 chưa được cài. Cài Python 3.10+ rồi chạy lại."
  exit 1
fi

# Check requirements
if ! python3 -c "import fastapi" 2>/dev/null; then
  echo "⚠ Chưa cài requirements. Đang cài..."
  python3 -m pip install -r requirements.txt
fi

# Run from backend/ so the imports work (main.py uses `import db`, not `from backend import db`)
cd backend
echo "🚀 Khởi động BalanceBuddy AI tại http://localhost:8000 ..."
exec python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
