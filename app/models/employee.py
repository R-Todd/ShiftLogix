from datetime import datetime
from app import db, bcrypt
from flask_jwt_extended import create_access_token

class Employee(db.Model):
    __tablename__ = "employees"

    userId    = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String(80), nullable=False)
    email     = db.Column(db.String(120), unique=True, nullable=False)
    password  = db.Column(db.String(255), nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    shifts    = db.relationship("Shift", backref="employee", lazy=True)
    requests  = db.relationship("ShiftChange", backref="requester", lazy=True)

    def set_password(self, raw):
        self.password = bcrypt.generate_password_hash(raw).decode("utf-8")

    def check_password(self, raw):
        return bcrypt.check_password_hash(self.password, raw)

    def create_token(self):
        return create_access_token(identity=self.userId)
