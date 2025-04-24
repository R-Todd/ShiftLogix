"""
File: clock_service/app/routes/clock_routes.py
Purpose: Provides endpoints for employee clock-in and clock-out.
"""

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Timesheet
from datetime import datetime

clock_bp = Blueprint("clock", __name__, url_prefix="/api/clock")

@clock_bp.route("/in", methods=["POST"])
@jwt_required()
def clock_in():
    employee_id = get_jwt_identity()

    # ✅ Check for existing open clock-in
    existing = Timesheet.query.filter_by(employee_id=employee_id, clock_out=None).first()
    if existing:
        return jsonify({
            "success": False,
            "message": "You are already clocked in. Please clock out before clocking in again."
        }), 400

    #  Create new clock-in entry
    new_entry = Timesheet(employee_id=employee_id)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Clock-in recorded.",
        "timesheetId": new_entry.timesheetId
    }), 200


@clock_bp.route("/out", methods=["POST"])
@jwt_required()
def clock_out():
    employee_id = get_jwt_identity()

    entry = Timesheet.query.filter_by(employee_id=employee_id, clock_out=None)\
                           .order_by(Timesheet.clock_in.desc()).first()
    if not entry:
        return jsonify({"success": False, "message": "No active clock-in found."}), 404

    entry.clock_out = datetime.utcnow()
    db.session.commit()

    return jsonify({"success": True, "message": "Clock-out recorded."}), 200
