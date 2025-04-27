def validate_clock(userId, password):
    """
    Validates the clock in/out form input.

    Parameters:
      - userId: The user's ID (expected to be numeric)
      - password: The user's password (non-empty)

    Returns:
      - A tuple (is_valid, message) where is_valid is a boolean indicating if validation passed,
        and message contains error details if validation fails.
    """
    if not userId or not password:
        return False, "Both UserId and Password are required."
    try:
        int(userId)
    except ValueError:
        return False, "UserId must be a valid number."
    return True, "Validation passed."
