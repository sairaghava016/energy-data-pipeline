import boto3
import json
import random
import uuid
from datetime import datetime

BUCKET_NAME = 'energy-data-pipeline-sai'
s3 = boto3.client('s3')

def generate_data():
    data = []
    for i in range(5):
        site_id = f"site_{str(i).zfill(3)}"
        record = {
            "site_id": site_id,
            "timestamp": datetime.utcnow().isoformat(),
            "energy_generated_kwh": round(random.uniform(50, 200), 2),
            "energy_consumed_kwh": round(random.uniform(40, 180), 2)
        }
        data.append(record)
    return data

def upload_to_s3(data):
    file_name = f"data/energy_data_{uuid.uuid4()}.json"
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(data)
    )
    print(f"Uploaded: {file_name}")
