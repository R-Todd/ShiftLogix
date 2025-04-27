class AvailabilityService:
    def __init__(self, repo):
        self.repo = repo

    def update(self, employee_id, day, availability):
        # stub: store request in ShiftChange
        return f"Availability for {day} set to {availability}"

    def list_requests(self, employee_id):
        # stub: return list of request objects
        return []