from flask import Flask, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = "userfiles"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

@app.route("/")
def index():
    return "<html><body><h1>Hello, world!</h1></body></html>"

@app.route("/home")
def home():
    return "<html><body><h1>Ahi and Ved are the coolest kids ever!</h1><p>They love adventures, coding, and making everyone smile.</p></body></html>"

@app.route("/office")
def office():
    return "<html><body><h1>Hello, world!</h1></body></html>"

@app.route("/file", methods=["GET", "POST"])
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
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
