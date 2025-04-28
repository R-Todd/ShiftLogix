"""
File: schedule_service/app/__init__.py
Purpose: Initializes Flask app, database, JWT, and routes.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from app.persistence.models import db

# Load environment variables from .env
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=env_path)

jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Load config from environment
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False") == "True"
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register routes (fixed paths)
    from app.presentation.schedule_routes import schedule_bp
    from app.presentation.availability_routes import availability_bp
    app.register_blueprint(schedule_bp, url_prefix="/api/schedule")
    app.register_blueprint(availability_bp, url_prefix="/api/availability")

    # Create tables if needed
    with app.app_context():
        db.create_all()

    return app
