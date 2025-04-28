"""
File: auth_service/app/application/auth_service.py
Purpose: Encapsulates all business logic related to user registration, login, and current user retrieval.
"""

from app import db
from app.persistence.models import Employee, bcrypt
from app.validators.validate_register import validate_register
from app.validators.log_in_validator import validate_log_in
from flask_jwt_extended import create_access_token
from datetime import timedelta

class AuthService:
    def register_user(self, data):
        """
        Handles user registration logic.
        """
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")

        # Validate input
        valid, message = validate_register(first_name, last_name, email, password)
        if not valid:
            raise ValueError(message)

        # Check for duplicate email
        if Employee.query.filter_by(email=email).first():
            raise ValueError("Email already registered.")

        # Create new user
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = Employee(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password_hash=hashed_password,
            role="Employee"
        )

        # Save to database
        db.session.add(new_user)
        db.session.commit()

        return new_user.userId

    def login_user(self, data):
        """
        Handles user login logic and JWT token generation.
        """
        email = data.get("email")
        password = data.get("password")

        # Validate input
        valid, message = validate_log_in(email, password)
        if not valid:
            raise ValueError(message)

        # Authenticate user
        user = Employee.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            raise ValueError("Invalid credentials.")

        # Create JWT token
        access_token = create_access_token(
            identity=str(user.userId),
            expires_delta=timedelta(hours=1)
        )
        return access_token

    def get_current_user(self, user_id):
        """
        Retrieves the current logged-in user's profile data.
        """
        user = Employee.query.get(user_id)
        if not user:
            raise ValueError("User not found.")

        return {
            "userId": user.userId,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "role": user.role
        }
