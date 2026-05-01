from flask import Flask
from config import UPLOAD_FOLDER, MAX_FILE_SIZE

def create_app():
    """Create and configure Flask app"""
    app = Flask(__name__)
    
    # Configuration
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE
    
    # Register blueprints
    from routes.basic import basic_bp
    from routes.file_upload import file_bp
    from routes.chat import chat_bp
    
    app.register_blueprint(basic_bp)
    app.register_blueprint(file_bp)
    app.register_blueprint(chat_bp)
    
    return app
