import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_identity
from flask_bcrypt import Bcrypt

# instantiate extensions
db      = SQLAlchemy()
migrate = Migrate()
jwt     = JWTManager()
bcrypt  = Bcrypt()

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.getcwd(), "app", "templates"),
        static_folder=  os.path.join(os.getcwd(), "app", "static"),
    )

    # ─── Core Flask config ─────────────────────────────────────────────────────
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-change-me-please")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///shiftlogix.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ─── JWT config ────────────────────────────────────────────────────────────
    app.config["JWT_SECRET_KEY"]       = os.getenv("JWT_SECRET_KEY", "also-change-this")
    app.config["JWT_TOKEN_LOCATION"]   = ["cookies"]
    app.config["JWT_ACCESS_COOKIE_PATH"]   = "/"
    app.config["JWT_REFRESH_COOKIE_PATH"]  = "/"
    app.config["JWT_COOKIE_SECURE"]        = False
    app.config["JWT_COOKIE_CSRF_PROTECT"]  = False
    app.config["JWT_COOKIE_SAMESITE"]      = "Lax"

    # ─── Initialize extensions ─────────────────────────────────────────────────
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # ─── inject current_user into all templates ─────────────────────────────────
    @app.context_processor
    def inject_current_user():
        try:
            # optional verify; will not raise if no JWT
            verify_jwt_in_request(optional=True)
            uid = get_jwt_identity()
        except Exception:
            uid = None
        return {"current_user": uid}

    # ─── Register blueprints ────────────────────────────────────────────────────
    from app.controllers.auth_controller             import auth_bp
    from app.controllers.home_controller             import home_bp
    from app.controllers.register_controller         import register_bp
    from app.controllers.clock_controller            import clock_bp
    from app.controllers.schedule_controller         import schedule_bp
    from app.controllers.availability_controller     import availability_bp
    from app.controllers.employee_dashboard_controller import employee_dashboard_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(clock_bp)
    app.register_blueprint(schedule_bp)
    app.register_blueprint(availability_bp)
    app.register_blueprint(employee_dashboard_bp)

    return app
