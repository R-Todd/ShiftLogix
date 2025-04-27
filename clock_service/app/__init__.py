"""
File: clock_service/app/__init__.py
Purpose: Initializes Flask app, database, JWT, and routes.
"""

import os                                    # stdlib, for paths and env lookup
from flask import Flask                      # core web framework
from flask_jwt_extended import JWTManager    # JWT support
from dotenv import load_dotenv               # loads .env into os.environ

# Persistence layer: SQLAlchemy `db` instance
from app.persistence.models import db       


# Load environment variables
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=env_path)

jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Config from .env
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False") == "True"
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from app.presentation.clock_routes import clock_bp
    app.register_blueprint(clock_bp)

    # Create tables if needed
    with app.app_context():
        db.create_all()

    return app
