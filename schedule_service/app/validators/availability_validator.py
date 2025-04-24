from datetime import datetime

VALID_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def validate_availability(data):
    if not data.get("day_of_week") or not data.get("start_time") or not data.get("end_time"):
        return False, "All fields are required."

    if data["day_of_week"] not in VALID_DAYS:
        return False, "Invalid day_of_week."

    try:
        start_time = datetime.strptime(data["start_time"], "%H:%M").time()
        end_time = datetime.strptime(data["end_time"], "%H:%M").time()
    except ValueError:
        return False, "Invalid time format."

    if start_time >= end_time:
        return False, "Start time must be before end time."

    return True, None
