import os

# Flask Configuration
HOST = "0.0.0.0"
PORT = 8080

# File Upload Configuration
UPLOAD_FOLDER = "userfiles"
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# AI Configuration
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/gpt2"
HUGGINGFACE_API_TOKEN = "hf_default"
