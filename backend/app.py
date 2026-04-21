import os
import sys

# Add parent folder to path to allow absolute imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from config import Config

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join('..', 'frontend'),
        static_folder=os.path.join('..', 'frontend', 'static')
    )
    
    app.config.from_object(Config)

    from backend.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)