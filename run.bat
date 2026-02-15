@echo off
echo Activating virtual environment...
call .venv\Scripts\activate

echo Starting FastAPI server...
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

pause