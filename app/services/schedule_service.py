from app.ports.shift_repository import ShiftRepository

class ScheduleService:
    def __init__(self, repo: ShiftRepository):
        self.repo = repo

    def list_for(self, employee_id: int):
        return self.repo.list_shifts(employee_id)

    def create_for(self, employee_id: int, start_time, end_time):
        return self.repo.add_shift(employee_id, start_time, end_time)