import os
from flask import Flask
from app.presentation.ui_routes import ui_bp
from app.presentation.auth_proxy import auth_bp
from app.presentation.clock_proxy import clock_bp
from app.presentation.schedule_proxy import schedule_bp
from app.presentation.availability_proxy import availability_bp


def create_app():
    app = Flask(__name__, template_folder="templates")

    # Load secret key from .env or default
    app.secret_key = os.getenv("SECRET_KEY", "change-me-please")

    # Register Blueprints
    app.register_blueprint(ui_bp)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(clock_bp, url_prefix="/api/clock")
    app.register_blueprint(schedule_bp, url_prefix="/api/schedule")
    app.register_blueprint(availability_bp, url_prefix="/api/availability")

    return app
