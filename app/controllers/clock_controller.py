from flask import Blueprint, render_template, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.schedule_service import ScheduleService

def create_clock_blueprint(shift_repo):
    from app.services.clock_service import ClockService
    clock_svc = ClockService(shift_repo)
    bp = Blueprint("clock", __name__, url_prefix="/clock")

    @bp.route("/", methods=["GET", "POST"])
    @jwt_required()
    def clock_view():
        user_id = int(get_jwt_identity())
        if request.method == "POST":
            start = request.form['start']
            end   = request.form['end']
            clock_svc.record(user_id, start, end)
        shifts = clock_svc.list(user_id)
        return render_template("clock.html", shifts=shifts)

    return bp