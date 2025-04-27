from app.models.shift import Shift
from app import db

class ScheduleService:
    def get_all_shifts(self):
        return Shift.query.order_by(Shift.start_time).all()

    def create_shift(self, start_time, end_time, employee_id):
        shift = Shift(
            start_time  = start_time,
            end_time    = end_time,
            employee_id = employee_id
        )
        db.session.add(shift)
        db.session.commit()
        return shift
