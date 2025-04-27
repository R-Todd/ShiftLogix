from app.models.shift_change import ShiftChange
from app import db

class AvailabilityService:
    def get_employee_availability(self, emp_id):
        # assuming ShiftChange stores availability requests
        return ShiftChange.query.filter_by(employee_id=emp_id).all()

    def set_availability(self, emp_id, day, available):
        # for demo, treat like a change request
        req = ShiftChange(
            shift_id    = 0,
            add_or_drop = "add" if available else "drop",
            employee_id = emp_id,
            reason      = f"{day}-availability",
            status      = "pending"
        )
        db.session.add(req)
        db.session.commit()
        return req
