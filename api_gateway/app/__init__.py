#apigateway/app/__init__.py
import os
from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

# Load gateway’s .env (with JWT_SECRET_KEY & service URLs)
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

def create_app():
    app = Flask(__name__, template_folder="templates")
    # 2️Flask session secret (fallback)
    app.secret_key = os.getenv("SECRET_KEY", "change-me-please")
    # 3️ JWT setup
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    JWTManager(app)

    # 4️ Register Blueprints (all proxies & UI)
    from app.presentation.ui_routes import ui_bp
    from app.presentation.auth_proxy import auth_bp
    from app.presentation.clock_proxy import clock_bp
    from app.presentation.schedule_proxy import schedule_bp
    from app.presentation.availability_proxy import availability_bp

    app.register_blueprint(ui_bp)
    app.register_blueprint(auth_bp,         url_prefix="/api/auth")
    app.register_blueprint(clock_bp,        url_prefix="/api/clock")
    app.register_blueprint(schedule_bp,     url_prefix="/api/schedule")
    app.register_blueprint(availability_bp, url_prefix="/api/availability")

    return app

