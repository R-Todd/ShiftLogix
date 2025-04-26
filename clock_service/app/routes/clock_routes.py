"""
File: clock_service/app/routes/clock_routes.py
Purpose: Provides endpoints for employee clock-in and clock-out.
UPDATED: Refactor to Layered Architecture for Clock Service
    - Moved business logic from routes to TimesheetService class in new services layer.
    - Improved error handling by raising and catching ValueError exceptions.
    - Cleaned up routes to handle only HTTP request/response formatting.
    - Improved overall code readability, maintainability, and separation of concerns.
"""

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.timesheet_service import TimesheetService


# Initialize the clock blueprint
# This blueprint will handle all routes related to clocking in and out for employees."""
clock_bp = Blueprint('clock', __name__, url_prefix='/api/clock')

@clock_bp.route('/in', methods=['POST'])
@jwt_required()
def clock_in():
    """
    Endpoint for employee clock-in.
    Expects a POST request with JWT token in the header.
    Returns the new Timesheet entry on success.
    """
    employee_id = get_jwt_identity()
    service = TimesheetService()

    try:
         ## Call the service to clock in the employee
        new_entry = service.clock_in(employee_id)
        # If successful, return the new Timesheet entry as JSON
        return jsonify(new_entry.to_dict()), 201
    except ValueError as e:
        # If the service raises an error (already clocked in), return 400
        return jsonify({"error": str(e)}), 400
