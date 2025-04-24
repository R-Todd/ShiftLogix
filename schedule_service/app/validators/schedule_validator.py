from datetime import datetime, date, time

def validate_shift_request(data):
    required_fields = ["request_type", "shift_date", "start_time", "end_time"]
    for field in required_fields:
        if not data.get(field):
            return False, f"Missing field: {field}"

    try:
        shift_date = datetime.strptime(data["shift_date"], "%Y-%m-%d").date()
        start_time = datetime.strptime(data["start_time"], "%H:%M").time()
        end_time = datetime.strptime(data["end_time"], "%H:%M").time()
    except ValueError:
        return False, "Invalid date or time format."

    if shift_date < date.today():
        return False, "Shift date cannot be in the past."

    if start_time >= end_time:
        return False, "Start time must be before end time."

    if data["request_type"] not in ["add", "drop"]:
        return False, "Invalid request_type. Use 'add' or 'drop'."

    return True, None
