import boto3
import os
import subprocess
from delete_audio import delete_audio

SOURCE_BUCKET = "your-audio-bucket"
DESTINATION_FOLDER = "converted_audio/"

def lambda_handler(event, context):
    try:
        action = event.get("action", "process")
        user_id = event.get("user_id")
        file_name = event.get("file_name")

        if action == "cancel":
            result = delete_audio(user_id, file_name)
            return {
                "statusCode": 200 if result else 500,
                "body": f"Cancel {'succeeded' if result else 'failed'}"
            }

        s3_key = f"original_audio/{user_id}/{file_name}"
        base_name, _ = os.path.splitext(file_name)
        converted_name = f"{base_name}_converted.wav"
        local_input = f"/tmp/{file_name}"
        local_output = f"/tmp/{converted_name}"

        s3_client = boto3.client("s3")
        s3_client.download_file(SOURCE_BUCKET, s3_key, local_input)

        command = f"/opt/bin/ffmpeg -i {local_input} -b:a 192k {local_output}"
        subprocess.run(command, shell=True, check=True)

        converted_key = f"{DESTINATION_FOLDER}{converted_name}"
        s3_client.upload_file(local_output, SOURCE_BUCKET, converted_key)

        return {
            "statusCode": 200,
            "body": f"Converted and uploaded: {converted_key}"
        }

    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
