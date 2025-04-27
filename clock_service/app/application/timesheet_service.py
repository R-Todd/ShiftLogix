# clock_service/app/services/timesheet_service.py

from datetime import datetime, timezone
from app.persistence.models import db, Timesheet

class TimesheetService:
    """
    Service class responsible for Timesheet operations.
    """

    def clock_in(self, employee_id):
        """
        Clock in the employee by creating a new Timesheet entry.
        Raises ValueError if the employee is already clocked in.
        """
        # Check for an existing open clock-in
        existing = Timesheet.query.filter_by(
            employee_id=employee_id,
            clock_out=None
        ).first()
        if existing:
            raise ValueError(
                "You are already clocked in. "
                "Please clock out before clocking in again."
            )

        # Corrected: use datetime.now(timezone.utc)
        new_entry = Timesheet(
            employee_id=employee_id,
            clock_in=datetime.now(timezone.utc)
        )

        db.session.add(new_entry)
        db.session.commit()
        return new_entry

    def clock_out(self, employee_id):
        """
        Clock out the employee by setting the clock_out on the latest open entry.
        Raises ValueError if no active clock-in is found.
        """
        entry = (
            Timesheet.query
            .filter_by(employee_id=employee_id, clock_out=None)
            .order_by(Timesheet.clock_in.desc())
            .first()
        )
        if not entry:
            raise ValueError("No active clock-in found. Please clock in first.")

        # Corrected: use datetime.now(timezone.utc) as well
        entry.clock_out = datetime.now(timezone.utc)
        db.session.commit()
        return entry
