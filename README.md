# 🎧 AWS Audio Processing Pipeline

A modular Python toolkit that uploads, converts, and deletes audio files using Amazon S3 and AWS Lambda.

## 🚀 Features
- 📤 Upload audio files to an S3 bucket (`upload_audio.py`)
- 🔁 Convert audio format (e.g., `.mp3` → `.wav`) using AWS Lambda (`convert_audio.py` + `lambda_function.py`)
- ❌ Cancel or delete uploads from S3 (`delete_audio.py`)
- 🔄 Dual-trigger Lambda handler: supports both HTTP (API Gateway) and S3 event inputs

## 🧩 Modules
| File               | Purpose                                |
|--------------------|----------------------------------------|
| `upload_audio.py`  | Uploads audio to S3                    |
| `convert_audio.py` | Triggers Lambda for format conversion |
| `delete_audio.py`  | Deletes S3 files                      |
| `lambda_function.py` | Lambda logic for FFmpeg conversion |

## 🛠 Setup

### 1. Create a `.env` or configure AWS CLI
Ensure your AWS credentials are set in the environment or AWS CLI.

### 2. Install dependencies
```bash
pip install boto3
```

### 3. Deploy Lambda
- Include `ffmpeg` via AWS Lambda layer or package with Docker
- Ensure Lambda has permissions to read/write S3

### 4. Test Locally
Update user/file info and run:
```bash
python upload_audio.py
python convert_audio.py
python delete_audio.py
```

## 🛡 Disclaimer
For demo use only. Validate file type, sanitize user input, and apply IAM permissions for production use.

## 📄 License
MIT