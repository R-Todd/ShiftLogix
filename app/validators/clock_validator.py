from datetime import datetime

def validate_clock(form):
    errors = []
    try:
        start = datetime.fromisoformat(form["start"])
        end   = datetime.fromisoformat(form["end"])
        if end <= start:
            errors.append("End must be after start.")
    except Exception:
        errors.append("Invalid date/time format.")
        return None, None, errors
    return start, end, errors
