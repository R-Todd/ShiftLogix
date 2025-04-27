from datetime import datetime
from app import db

class Shift(db.Model):
    __tablename__ = "shifts"

    shiftId    = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time   = db.Column(db.DateTime, nullable=False)
    employee_id= db.Column(db.Integer, db.ForeignKey("employees.userId"), nullable=False)

    def duration(self):
        return self.end_time - self.start_time

    def __repr__(self):
        return f"<Shift {self.shiftId} for Employee {self.employee_id}>"
