from flask import Blueprint, request, current_app
from werkzeug.utils import secure_filename
import os

file_bp = Blueprint('file', __name__)

@file_bp.route("/file", methods=["GET", "POST"])
def file_upload():
    if request.method == "POST":
        # Check if file is in request
        if "file" not in request.files:
            return "<html><body><h1>Error</h1><p>No file provided</p><a href='/file'>Go back</a></body></html>", 400
        
        file = request.files["file"]
        if file.filename == "":
            return "<html><body><h1>Error</h1><p>No file selected</p><a href='/file'>Go back</a></body></html>", 400
        
        # Save file
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        return f"<html><body><h1>Success!</h1><p>File '{filename}' uploaded to /userfiles</p><a href='/file'>Upload another file</a></body></html>"
    
    # GET request - show upload form
    return """<html><body>
    <h1>File Upload</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>
    </body></html>"""
