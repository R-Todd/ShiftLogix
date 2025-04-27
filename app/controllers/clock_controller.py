from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.validators.clock_validator import validate_clock
from app.models.shift import Shift
from app import db

clock_bp = Blueprint("clock", __name__, url_prefix="/clock")

@clock_bp.route("/", methods=["GET", "POST"])
@jwt_required()
def clock_view():
    user_id = get_jwt_identity()
    if request.method == "POST":
        start, end, errors = validate_clock(request.form)
        if errors:
            for e in errors: flash(e, "danger")
        else:
            shift = Shift(start_time=start, end_time=end, employee_id=user_id)
            db.session.add(shift)
            db.session.commit()
            flash("Shift recorded", "success")
        return redirect(url_for("clock.clock_view"))
    shifts = Shift.query.filter_by(employee_id=user_id).all()
    return render_template("clock.html", shifts=shifts)
