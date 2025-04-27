from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.availability_service import AvailabilityService

def create_availability_blueprint(shift_repo):
    bp = Blueprint("availability", __name__, url_prefix="/availability")
    avail_svc = AvailabilityService(shift_repo)

    @bp.route("/", methods=["GET", "POST"])
    @jwt_required()
    def availability_view():
        user_id = int(get_jwt_identity())
        if request.method == "POST":
            day   = request.form['day_of_week']
            avail = 'yes' if request.form.get('is_available') else 'no'
            flash(avail_svc.update(user_id, day, avail), 'success')
            return redirect(url_for('availability.availability_view'))
        slots = avail_svc.list_requests(user_id)
        return render_template('availability.html', slots=slots)

    return bp