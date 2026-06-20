from flask import Flask
from app.infrastructure.config import Config

def create_app():
    app = Flask(__name__)
    
    # Chargement de la configuration
    app.config.from_object(Config)
    
    # Enregistrement des routes
    from app.infrastructure.web.routes import web_blueprint
    app.register_blueprint(web_blueprint)
    
    return app