from fastapi import FastAPI, UploadFile, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from local_fp import process_local_and_save
from aws_glue_trigger import presign_url, start_glue_job
import uuid

app = FastAPI()

# CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/presign")
def get_presign(filename: str):
    return presign_url(filename)

@app.post("/process/local")
async def process_local(background_tasks: BackgroundTasks, file: UploadFile, min_support: float = 0.05, min_conf: float = 0.5):
    job_id = str(uuid.uuid4())
    background_tasks.add_task(process_local_and_save, file.file, min_support, min_conf, job_id)
    return {"job_id": job_id}

@app.post("/process/glue")
def process_glue(s3_key: str, min_support: float = 0.05, min_conf: float = 0.5):
    job_id = str(uuid.uuid4())
    run_id = start_glue_job(s3_key, job_id, min_support, min_conf)
    return {"job_id": job_id, "glue_run_id": run_id}
