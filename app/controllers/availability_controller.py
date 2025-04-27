from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.availability_service import AvailabilityService

availability_bp = Blueprint("availability", __name__, url_prefix="/availability")
svc             = AvailabilityService()

@availability_bp.route("/", methods=["GET", "POST"])
@jwt_required()
def availability_view():
    user_id = get_jwt_identity()
    if request.method == "POST":
        day   = request.form["day_of_week"]
        avail= bool(request.form.get("is_available"))
        svc.set_availability(user_id, day, avail)
        flash("Availability updated", "success")
        return redirect(url_for("availability.availability_view"))
    slots = svc.get_employee_availability(user_id)
    return render_template("availability.html", slots=slots)
