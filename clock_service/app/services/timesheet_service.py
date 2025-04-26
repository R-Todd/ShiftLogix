# clock_service/app/services/timesheet_service.py


from app.models import db, Timesheet
from datetime import datetime

class TimesheetService:
    def clock_in(self, employee_id):
        """
        Clock in the employee by creating a new Timesheet entry.
        """
        # Check for existing open clock-in
        existing = Timesheet.query.filter_by(employee_id=employee_id, clock_out=None).first()
        if existing:
            raise ValueError("You are already clocked in. Please clock out before clocking in again.")
            

        # create new clock-in entry
        new_entry = Timesheet(employee_id=employee_id, clock_in=datetime.now(datetime.timezone.utc))
        # Add the new entry to the session and commit
        db.session.add(new_entry)
        db.session.commit()

        return new_entry
    
    def clock_out(self, employee_id):
        """
        Clock out the employee by updating the latest Timesheet entry.
        """
        # Get the latest clock-in entry for the employee
        entry = Timesheet.query.filter_by(employee_id=employee_id, clock_out=None)\
                               .order_by(Timesheet.clock_in.desc()).first()
        if not entry:
            raise ValueError("No active clock-in found.")

        # Update the clock-out time
        entry.clock_out = datetime.utcnow()
        db.session.commit()

        return entry