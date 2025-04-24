from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Shift, ShiftChange
from datetime import datetime
from app.validators.schedule_validator import validate_shift_request

schedule_bp = Blueprint("schedule_bp", __name__, url_prefix="/schedule")

@schedule_bp.route("/shifts", methods=["GET"])
@jwt_required()
def get_shifts():
    employee_id = get_jwt_identity()
    shifts = Shift.query.filter_by(employee_id=employee_id).all()

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
    shift_date = datetime.strptime(data["shift_date"], "%Y-%m-%d").date()
    start_time = datetime.strptime(data["start_time"], "%H:%M").time()
    end_time = datetime.strptime(data["end_time"], "%H:%M").time()

    new_request = ShiftChange(
        employee_id=employee_id,
        request_type=data["request_type"],
        shift_date=shift_date,
        start_time=start_time,
        end_time=end_time
    )

    db.session.add(new_request)
    db.session.commit()

    return jsonify({"success": True, "message": "Shift change request submitted."}), 200
