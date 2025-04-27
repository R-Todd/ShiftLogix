from datetime import datetime

class ClockService:
    def __init__(self, repo):
        self.repo = repo

    def record(self, employee_id, start_iso, end_iso):
        start = datetime.fromisoformat(start_iso)
        end   = datetime.fromisoformat(end_iso)
        return self.repo.add_shift(employee_id, start, end)

    def list(self, employee_id):
        return self.repo.list_shifts(employee_id)