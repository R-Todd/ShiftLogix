from app import db, bcrypt
from datetime import datetime

class Employee(db.Model):
    userId    = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String(128), nullable=False)
    email     = db.Column(db.String(128), unique=True, nullable=False)
    password  = db.Column(db.String(128), nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, raw):
        self.password = bcrypt.generate_password_hash(raw).decode('utf-8')

    def check_password(self, raw):
        return bcrypt.check_password_hash(self.password, raw)