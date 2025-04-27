from app.ports.auth_service import AuthService
from app.models.employee import Employee
from flask_jwt_extended import create_access_token

class JWTAuthAdapter(AuthService):
    def authenticate(self, email: str, password: str) -> str:
        user = Employee.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            raise ValueError("Invalid credentials")
        return create_access_token(identity=str(user.userId))