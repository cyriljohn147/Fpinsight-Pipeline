import boto3, uuid, os

s3 = boto3.client("s3")
glue = boto3.client("glue")
BUCKET = os.getenv("AWS_BUCKET_NAME", "retail-dataset-cyril")
GLUE_JOB_NAME = os.getenv("AWS_GLUE_JOB", "fp-growth-job")

def presign_url(filename: str):
    key = f"uploads/{uuid.uuid4()}_{filename}"
    post = s3.generate_presigned_post(BUCKET, key, ExpiresIn=3600)
    return {"s3_key": key, "presign": post}

def start_glue_job(s3_key: str, job_id: str, min_support: float, min_conf: float):
    run = glue.start_job_run(
        JobName=GLUE_JOB_NAME,
        Arguments={
            '--INPUT_S3': f"s3://{BUCKET}/{s3_key}",
            '--OUTPUT_S3': f"s3://{BUCKET}/results/{job_id}",
            '--MIN_SUPPORT': str(min_support),
            '--MIN_CONF': str(min_conf)
        }
    )
    return run['JobRunId']
