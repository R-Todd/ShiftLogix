"""
File: auth_service/app/validators/log_in_validator.py
Purpose: Provides validation functions for user login credentials.
"""

import re

def validate_log_in(email, password):
    """
    Validates login credentials.

    Parameters:
        email (str): User's email address.
        password (str): User's password.

    Returns:
        tuple: (bool, str)
            - True, "" if valid
            - False, error message if invalid
    """
    # Check if email and password were provided
    if not email or not password:
        return False, "Email and password are required."

    # Validate email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        return False, "Invalid email format."

    # Check minimum password length
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."

    # Optional: Add complexity check
    # Example: require at least one digit or special character
    if not re.search(r"[0-9!@#$%^&*]", password):
        return False, "Password must contain at least one number or special character."

    return True, ""
