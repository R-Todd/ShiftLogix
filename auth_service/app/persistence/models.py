"""
File: auth_service/app/models.py
Purpose: Defines the Employee model used for authentication and registration.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# These will be initialized in app/__init__.py
db = SQLAlchemy()
bcrypt = Bcrypt()

class Employee(db.Model):
    __tablename__ = "employees"

    userId = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="Employee")

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Employee {self.userId}: {self.first_name} {self.last_name} ({self.role})>"
