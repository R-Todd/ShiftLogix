# File: schedule_service/app/presentation/availability_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.application.availability_service import AvailabilityService
from app.validators.availability_validator import validate_availability

availability_bp = Blueprint("availability_bp", __name__, url_prefix="/availability")

@availability_bp.route("/", methods=["GET"])
@jwt_required()
def get_availability():
    employee_id = get_jwt_identity()
    availabilities = AvailabilityService.get_availability(employee_id)

    return jsonify([{
        "day_of_week": a.day_of_week,
        "start_time": a.start_time.strftime('%H:%M'),
        "end_time": a.end_time.strftime('%H:%M')
    } for a in availabilities]), 200

@availability_bp.route("/", methods=["POST"])
@jwt_required()
def submit_availability():
    data = request.get_json() if request.is_json else request.form

    is_valid, error = validate_availability(data)
    if not is_valid:
        return jsonify({"success": False, "message": error}), 400

    employee_id = get_jwt_identity()

    try:
        AvailabilityService.post_availability(employee_id, data)
        return jsonify({"success": True, "message": "Availability saved."}), 200
    except ValueError as e:
        return jsonify({"success": False, "message": str(e)}), 400
