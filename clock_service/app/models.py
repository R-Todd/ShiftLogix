"""
File: clock_service/app/models.py
Purpose: Defines the Timesheet model for tracking employee clock-in/out.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Timesheet(db.Model):
    __tablename__ = "timesheets"


    # Primary Key: Unique ID for each timesheet record
    timesheetId = db.Column(db.Integer, primary_key=True)
    
    # Foreign Key reference: ID of the employee associated with this timesheet
    employee_id = db.Column(db.Integer, nullable=False)
    
    # Clock-in time (auto-set to current UTC time by default)
    clock_in = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Clock-out time (nullable because employee may not have clocked out yet)
    clock_out = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Timesheet {self.timesheetId} - Emp {self.employee_id}>"
    

     # ==============================================================
    # Added for Layered Architecture Support:
    # to_dict() method allows the Timesheet instance to be safely
    # converted to a dictionary for JSON API responses.
    #
    # Why? 
    # - Services (Application Layer) and Routes (Presentation Layer)
    #   should not manually serialize database models.
    # - Layer separation: Models only define schema + serialization helper.
    # ==============================================================
    def to_dict(self):
        """
        Convert the Timesheet instance to a dictionary.
        This is useful for API responses.
        """
        return {
            "timesheetId": self.timesheetId,
            "employee_id": self.employee_id,
            "clock_in": self.clock_in.isoformat() if self.clock_in else None,
            "clock_out": self.clock_out.isoformat() if self.clock_out else None,
        }
