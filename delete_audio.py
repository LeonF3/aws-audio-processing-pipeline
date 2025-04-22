import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

AWS_REGION = "us-east-2"
S3_BUCKET = "your-audio-bucket"

s3_client = boto3.client("s3", region_name=AWS_REGION)

def delete_audio(user_id, file_name, prefix="original_audio/"):
    s3_key = f"{prefix}{user_id}/{file_name}"
    try:
        s3_client.delete_object(Bucket=S3_BUCKET, Key=s3_key)
        print(f"✅ Deleted: s3://{S3_BUCKET}/{s3_key}")
        return True
    except NoCredentialsError:
        print("❌ AWS credentials not found.")
    except PartialCredentialsError:
        print("❌ Incomplete AWS credentials.")
    except Exception as e:
        print(f"❌ Deletion error: {e}")
    return False

if __name__ == "__main__":
    delete_audio("user123", "sample.mp3")
