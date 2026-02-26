# Financial Document Analyzer

Candidate: ARPAN ARI

This project is a debugged and improved version of a financial document analyzer built using CrewAI and FastAPI.

The system analyzes financial PDF documents and provides financial insights.

---

# Features

✔ Upload Financial Documents (PDF)

✔ AI Financial Analysis

✔ Async Processing

✔ Queue Worker Model

✔ Database Storage

✔ Output Saving

✔ REST API

---

# Bugs Found and Fixed

## 1 Broken CrewAI Tools

Problem:

Tools were not compatible with CrewAI version.

Fix:

Reimplemented tools and analysis pipeline.

---

## 2 Celery Worker Not Loading

Problem:

Celery could not find module workers.worker.

Fix:

Created proper folder structure and __init__.py files.

---

## 3 Result Backend Disabled

Problem:

Celery results were not stored.

Error:

DisabledBackend object error.

Fix:

Enabled Redis backend:

broker=redis://localhost:6379/0
backend=redis://localhost:6379/0

---

## 4 API Server Errors

Problem:

GET /result caused 500 error.

Fix:

Added proper state checking.

---

## 5 Missing Environment Variables

Problem:

OpenAI API key missing.

Fix:

Added .env support.

---

## 6 Output Not Saved

Problem:

Results were not stored.

Fix:

Added outputs folder saving.

---

# Setup Instructions

## Step 1 Install
pip install -r requirements.txt

---

## Step 2 Start Redis
redis-server.exe

---

## Step 3 Start Worker
celery -A workers.worker worker --pool=solo --loglevel=info

---

## Step 4 Start API
uvicorn app.main:app --reload

---

# API Documentation

Open: http://127.0.0.1:8000/docs

---

# Endpoints

## Health Check

GET /

Response:
{
"status":"Financial Analyzer Running"
}

---

## Analyze Document

POST /analyze

Upload PDF.

Response:
{
"status":"processing",
"task_id":"xxxxx"
}

---

## Get Result

GET /result/{task_id}

Response:
{
"status":"completed",
"result":"Financial analysis..."
}

---

---

# Queue Worker Model

System uses:

Celery + Redis

Architecture:

User Upload → API → Redis Queue → Worker → Result

Supports concurrent requests.

---

# Database Integration

SQLite database:

analysis.db

Stores:

• Filename

• Query

• Result

---

# Output Files

Saved in:

outputs/

Example:

outputs/file123.txt

---

# Technologies Used

FastAPI

CrewAI

Celery

Redis

SQLite

LangChain

---

# Result

The system is fully functional and production-ready.


