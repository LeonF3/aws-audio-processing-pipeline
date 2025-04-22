import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

AWS_REGION = "us-east-2"
S3_BUCKET = "your-audio-bucket"

s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_audio(file_path, user_id, file_name):
    s3_key = f"original_audio/{user_id}/{file_name}"
    try:
        s3_client.upload_file(file_path, S3_BUCKET, s3_key)
        print(f"✅ Uploaded: s3://{S3_BUCKET}/{s3_key}")
        return f"s3://{S3_BUCKET}/{s3_key}"
    except NoCredentialsError:
        print("❌ AWS credentials not found.")
    except PartialCredentialsError:
        print("❌ Incomplete AWS credentials.")
    except Exception as e:
        print(f"❌ Upload error: {e}")
    return None

if __name__ == "__main__":
    upload_audio("sample.mp3", "user123", "sample.mp3")
