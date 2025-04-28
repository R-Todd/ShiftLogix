# File: schedule_service/app/application/availability_service.py
# Purpose: Business logic for managing employee availability.

from app.persistence.models import db, Availability
from app.validators.availability_validator import validate_availability

class AvailabilityService:

    @staticmethod
    def get_availability(employee_id):
        """
        Fetch all availability entries for the given employee.
        """
        return Availability.query.filter_by(employee_id=employee_id).all()

    @staticmethod
    def post_availability(employee_id, data):
        """
        Create or update availability entry for the employee for a specific day.
        """
        # Validate payload
        valid, message = validate_availability(data)
        if not valid:
            raise ValueError(message)

        day_of_week = data["day_of_week"]
        start_time = data["start_time"]
        end_time = data["end_time"]

        # Check if an entry already exists for this day
        existing = Availability.query.filter_by(employee_id=employee_id, day_of_week=day_of_week).first()
        
        if existing:
            # Update existing entry
            existing.start_time = start_time
            existing.end_time = end_time
        else:
            # Create new entry
            new_availability = Availability(
                employee_id=employee_id,
                day_of_week=day_of_week,
                start_time=start_time,
                end_time=end_time
            )
            db.session.add(new_availability)

        db.session.commit()
        return True
