# clock_service/app/services/timesheet_service.py

from app.models import db, Timesheet
from datetime import datetime, timezone


class TimesheetService:
    def clock_in(self, employee_id):
        """
        Clock in the employee by creating a new Timesheet entry.
        """
        # Check for existing open clock-in
        existing = Timesheet.query.filter_by(employee_id=employee_id, clock_out=None).first()
        if existing:
            raise ValueError("You are already clocked in. Please clock out before clocking in again.")

        # Create new clock-in entry with UTC timestamp
        new_entry = Timesheet(employee_id=employee_id, clock_in=datetime.datetime.now(datetime.timezone.utc))
        db.session.add(new_entry)
        db.session.commit()

        return new_entry

    def clock_out(self, employee_id):
        
        #Clock out the employee by updating the latest Timesheet entry.
        
        entry = Timesheet.query.filter_by(employee_id=employee_id, clock_out=None)\
                               .order_by(Timesheet.clock_in.desc()).first()
        if not entry:
            raise ValueError("No active clock-in found.")

        entry.clock_out = datetime.datetime.utcnow()
        db.session.commit()

        return entry
