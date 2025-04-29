# File: schedule_service/app/presentation/schedule_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.application.schedule_service import ScheduleService
from app.validators.schedule_validator import validate_shift_request

schedule_bp = Blueprint("schedule_bp", __name__, url_prefix="/api/schedule")

@schedule_bp.route("/shifts", methods=["GET"])
@jwt_required()
def get_shifts():
    employee_id = get_jwt_identity()
    shifts = ScheduleService.get_shifts(employee_id)

    return jsonify([{
        "date": s.date.strftime('%Y-%m-%d'),
        "start_time": s.start_time.strftime('%H:%M'),
        "end_time": s.end_time.strftime('%H:%M')
    } for s in shifts]), 200

@schedule_bp.route("/request", methods=["POST"])
@jwt_required()
def request_shift_change():
    data = request.get_json() if request.is_json else request.form

    is_valid, error = validate_shift_request(data)
    if not is_valid:
        return jsonify({"success": False, "message": error}), 400

    employee_id = get_jwt_identity()

    try:
        ScheduleService.submit_shift_request(employee_id, data)
        return jsonify({"success": True, "message": "Shift change request submitted."}), 200
    except ValueError as e:
        return jsonify({"success": False, "message": str(e)}), 400
