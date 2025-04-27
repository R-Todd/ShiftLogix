from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.schedule_service import ScheduleService

schedule_bp = Blueprint("schedule", __name__, url_prefix="/schedule")
svc         = ScheduleService()

@schedule_bp.route("/", methods=["GET", "POST"])
@jwt_required()
def schedule_view():
    user_id = get_jwt_identity()
    if request.method == "POST":
        svc.create_shift(
            start_time    = request.form["start_time"],
            end_time      = request.form["end_time"],
            employee_id   = user_id
        )
        flash("Shift added to schedule", "success")
        return redirect(url_for("schedule.schedule_view"))
    shifts = svc.get_all_shifts()
    return render_template("schedule.html", shifts=shifts)
