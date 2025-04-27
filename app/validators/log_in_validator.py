"""
File: ShiftLogix/backend/app/validators/log_in_validator.py
Purpose: Provides validation functions for user login credentials.
"""

import re  # For email validation

# ------------------------------ #
# LOGIN VALIDATION FUNCTION
# Ensures that email and password are properly formatted before login.
# ------------------------------ #
def validate_log_in(email, password):
    """
    Validates login credentials.
    
    Parameters:
        email (str): User's email address.
        password (str): User's password.
    
    Returns:
        tuple: (bool, str) - (True, "") if valid; (False, "Error message") if invalid.
    """
    if not email or not password:
        return False, "Email and password are required."

    # Validate email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        return False, "Invalid email format."

    # Ensure password length meets security standards
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."

    return True, ""
