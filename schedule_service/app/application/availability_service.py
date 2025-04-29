# File: schedule_service/app/application/availability_service.py
# Purpose: Business logic for managing employee availability.

from app.persistence.models import db, Availability
from app.validators.availability_validator import validate_availability
from datetime import datetime

class AvailabilityService:  # ← **wrap it in a class**

    @staticmethod
    def post_availability(employee_id, data):
        valid, message = validate_availability(data)
        if not valid:
            raise ValueError(message)

        day_of_week = data["day_of_week"]
        start_time = datetime.strptime(data["start_time"], "%H:%M").time()
        end_time = datetime.strptime(data["end_time"], "%H:%M").time()

        existing = Availability.query.filter_by(employee_id=employee_id, day_of_week=day_of_week).first()

        if existing:
            existing.start_time = start_time
            existing.end_time = end_time
        else:
            new_availability = Availability(
                employee_id=employee_id,
                day_of_week=day_of_week,
                start_time=start_time,
                end_time=end_time
            )
            db.session.add(new_availability)

        db.session.commit()
        return True

    @staticmethod
    def get_availability(employee_id):
        return Availability.query.filter_by(employee_id=employee_id).all()
