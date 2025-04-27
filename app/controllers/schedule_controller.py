from flask import Blueprint, render_template, request
from flask_jwt_extended import jwt_required, get_jwt_identity


def create_schedule_blueprint(schedule_service):
    bp = Blueprint("schedule", __name__, url_prefix="/schedule")

    @bp.route("/", methods=["GET", "POST"])
    @jwt_required()
    def schedule_view():
        user_id = int(get_jwt_identity())
        if request.method == "POST":
            start = request.form["start_time"]
            end   = request.form["end_time"]
            schedule_service.create_for(user_id, start, end)
        shifts = schedule_service.list_for(user_id)
        return render_template("schedule.html", shifts=shifts)

    return bp