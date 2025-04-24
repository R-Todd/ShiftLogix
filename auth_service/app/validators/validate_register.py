"""
File: auth_service/app/validators/validate_register.py
Purpose: Provides validation function for user registration input.
"""

import re

def validate_register(first_name, last_name, email, password):
    """
    Validates user registration input.

    Parameters:
        first_name (str): First name of the user
        last_name (str): Last name of the user
        email (str): Email address
        password (str): Password

    Returns:
        tuple: (bool, str)
            - True, "" if valid
            - False, error message if invalid
    """

    # Check all required fields
    if not all([first_name, last_name, email, password]):
        return False, "All fields are required."

    # First and last name validation (letters only)
    if not first_name.isalpha():
        return False, "First name must contain only letters."
    if not last_name.isalpha():
        return False, "Last name must contain only letters."

    # Email format validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        return False, "Invalid email format."

    # Password minimum length
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."

    # Password strength: at least one digit or special character
    if not re.search(r"[0-9!@#$%^&*]", password):
        return False, "Password must include at least one number or special character."

    return True, ""
