"""
File: clock_service/app/models.py
Purpose: Defines the Timesheet model for tracking employee clock-in/out.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Timesheet(db.Model):
    __tablename__ = "timesheets"

    timesheetId = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, nullable=False)
    clock_in = db.Column(db.DateTime, default=datetime.utcnow)
    clock_out = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Timesheet {self.timesheetId} - Emp {self.employee_id}>"
