def validate_login(form):
    errors = []
    if not form.get("email"):
        errors.append("Email required.")
    if not form.get("password"):
        errors.append("Password required.")
    return errors
