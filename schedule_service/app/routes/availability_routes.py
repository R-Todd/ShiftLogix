from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Availability
from datetime import datetime
from app.validators.availability_validator import validate_availability

availability_bp = Blueprint("availability_bp", __name__, url_prefix="/availability")

@availability_bp.route("/", methods=["GET"])
@jwt_required()
def get_availability():
    employee_id = get_jwt_identity()
    availabilities = Availability.query.filter_by(employee_id=employee_id).all()

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
    day = data["day_of_week"]
    start = datetime.strptime(data["start_time"], "%H:%M").time()
    end = datetime.strptime(data["end_time"], "%H:%M").time()

    existing = Availability.query.filter_by(employee_id=employee_id, day_of_week=day).first()

    if existing:
        existing.start_time = start
        existing.end_time = end
    else:
        new = Availability(
            employee_id=employee_id,
            day_of_week=day,
            start_time=start,
            end_time=end
        )
        db.session.add(new)

    db.session.commit()
    return jsonify({"success": True, "message": "Availability saved."}), 200
