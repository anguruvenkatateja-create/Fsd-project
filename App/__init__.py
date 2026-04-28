from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_key_123')

    # This part is crucial to avoid the ImportError
    with app.app_context():
        from . import routes
        return app