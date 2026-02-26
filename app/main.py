from fastapi import FastAPI, UploadFile, File, Form
import uuid
import os

from workers.worker import analyze_task
from celery.result import AsyncResult
from workers.worker import celery


app = FastAPI()


# -------------------------
# Root Endpoint
# -------------------------

@app.get("/")
def home():

    return {
        "status": "Financial Analyzer Running"
    }


# -------------------------
# Upload & Analyze PDF
# -------------------------

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    query: str = Form("Analyze this document")
):

    try:

        # Create data folder
        os.makedirs("data", exist_ok=True)

        # Generate unique file name
        file_id = str(uuid.uuid4())

        file_path = f"data/{file_id}.pdf"

        # Save file
        with open(file_path, "wb") as f:

            content = await file.read()

            f.write(content)

        # Send task to Celery worker
        task = analyze_task.delay(query, file_path)

        return {

            "status": "processing",

            "task_id": task.id

        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)

        }


# -------------------------
# Get Result
# -------------------------

@app.get("/result/{task_id}")
def result(task_id):

    try:

        res = AsyncResult(task_id, app=celery)

        # Still processing
        if res.state == "PENDING":

            return {

                "status": "processing",

                "result": None

            }

        # Completed
        if res.state == "SUCCESS":

            return {

                "status": "completed",

                "result": str(res.result)

            }

        # Failed
        if res.state == "FAILURE":

            return {

                "status": "failed",

                "result": str(res.result)

            }

        # Other states
        return {

            "status": res.state,

            "result": None

        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)

        }