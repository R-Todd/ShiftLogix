from app.ports.shift_repository import ShiftRepository
from app.models.shift import Shift
from app import db

class SQLAlchemyShiftRepository(ShiftRepository):
    def list_shifts(self, employee_id: int):
        return Shift.query.filter_by(employee_id=employee_id).all()

    def add_shift(self, employee_id: int, start_time, end_time):
        shift = Shift(employee_id=employee_id, start_time=start_time, end_time=end_time)
        db.session.add(shift)
        db.session.commit()
        return shift