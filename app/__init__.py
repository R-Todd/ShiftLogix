# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_identity
from flask_bcrypt import Bcrypt

# ─── Extensions ───────────────────────────────────────────────────────────────
db      = SQLAlchemy()
migrate = Migrate()
jwt     = JWTManager()
bcrypt  = Bcrypt()

# ─── Ports & Adapters imports ─────────────────────────────────────────────────
from app.adapters.sqlalchemy_shift_repo import SQLAlchemyShiftRepository
from app.adapters.jwt_auth_adapter      import JWTAuthAdapter
from app.services.schedule_service     import ScheduleService

# ─── Controller factory imports ────────────────────────────────────────────────
from app.controllers.auth_controller              import create_auth_blueprint
from app.controllers.register_controller          import create_register_blueprint
from app.controllers.home_controller              import create_home_blueprint
from app.controllers.employee_dashboard_controller import create_employee_dashboard_blueprint
from app.controllers.schedule_controller          import create_schedule_blueprint
from app.controllers.clock_controller             import create_clock_blueprint
from app.controllers.availability_controller      import create_availability_blueprint

def create_app():
    # ─── Flask app setup ────────────────────────────────────────────────────────
    app = Flask(
        __name__,
        template_folder=os.path.join(os.getcwd(), "app", "templates"),
        static_folder=os.path.join(os.getcwd(), "app", "static"),
    )

    # ─── Configuration ───────────────────────────────────────────────────────────
    app.config["SECRET_KEY"]                = os.getenv("SECRET_KEY", "dev-key")
    app.config["SQLALCHEMY_DATABASE_URI"]   = os.getenv("DATABASE_URL", "sqlite:///shiftlogix.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["JWT_SECRET_KEY"]       = os.getenv("JWT_SECRET_KEY", "jwt-secret")
    app.config["JWT_TOKEN_LOCATION"]   = ["cookies"]
    app.config["JWT_COOKIE_SECURE"]    = False
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False

    # ─── Initialize extensions ─────────────────────────────────────────────────
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # ─── Inject current_user into templates ──────────────────────────────────────
    @app.context_processor
    def inject_current_user():
        try:
            verify_jwt_in_request(optional=True)
            uid = get_jwt_identity()
        except Exception:
            uid = None
        return {"current_user": uid}

    # ─── Instantiate adapters & services ─────────────────────────────────────────
    shift_repo   = SQLAlchemyShiftRepository()
    auth_adapter = JWTAuthAdapter()
    schedule_svc = ScheduleService(shift_repo)

    # ─── Register blueprints ────────────────────────────────────────────────────
    app.register_blueprint(create_auth_blueprint(auth_adapter))
    app.register_blueprint(create_register_blueprint(auth_adapter))
    app.register_blueprint(create_home_blueprint())
    app.register_blueprint(create_employee_dashboard_blueprint(schedule_svc))
    app.register_blueprint(create_schedule_blueprint(schedule_svc))
    app.register_blueprint(create_clock_blueprint(shift_repo))
    app.register_blueprint(create_availability_blueprint(shift_repo))

    return app
