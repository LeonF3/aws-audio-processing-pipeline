import boto3
import json
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

AWS_REGION = "us-east-2"
LAMBDA_FUNCTION_NAME = "AudioFormatConversion"

lambda_client = boto3.client("lambda", region_name=AWS_REGION)

def convert_audio(user_id, file_name, target_format="wav"):
    payload = {
        "user_id": user_id,
        "file_name": file_name,
        "target_format": target_format
    }
    try:
        response = lambda_client.invoke(
            FunctionName=LAMBDA_FUNCTION_NAME,
            InvocationType="Event",
            Payload=json.dumps(payload)
        )
        print(f"✅ Lambda triggered for: {file_name}")
        return response
    except NoCredentialsError:
        print("❌ AWS credentials not found.")
    except PartialCredentialsError:
        print("❌ Incomplete AWS credentials.")
    except Exception as e:
        print(f"❌ Lambda error: {e}")
    return None

if __name__ == "__main__":
    convert_audio("user123", "sample.mp3")
