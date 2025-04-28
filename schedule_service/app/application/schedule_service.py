# File: schedule_service/app/application/schedule_service.py
# Purpose: Business logic for managing employee shifts and shift changes.

from app.persistence.models import db, Shift, ShiftChange
from app.validators.schedule_validator import validate_shift_request

class ScheduleService:

    @staticmethod
    def get_shifts(employee_id):
        """
        Fetch all assigned shifts for the given employee.
        """
        return Shift.query.filter_by(employee_id=employee_id).all()

    @staticmethod
    def submit_shift_request(employee_id, data):
        """
        Handle employee's request to add or drop a shift.
        """
        # Validate payload
        valid, message = validate_shift_request(data)
        if not valid:
            raise ValueError(message)

        request_type = data["request_type"]
        shift_date = data["shift_date"]
        start_time = data["start_time"]
        end_time = data["end_time"]

        # Create and save ShiftChange record
        shift_change = ShiftChange(
            employee_id=employee_id,
            request_type=request_type,
            shift_date=shift_date,
            start_time=start_time,
            end_time=end_time
        )

        db.session.add(shift_change)
        db.session.commit()
        return True
