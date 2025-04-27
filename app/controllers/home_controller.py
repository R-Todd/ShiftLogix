from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.employee import Employee

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def landing():
    # Always show the public landing page
    return render_template("home.html")

@home_bp.route("/dashboard")
@jwt_required()
def dashboard():
    # Always render the dashboard for logged-in users
    user_id  = get_jwt_identity()
    employee = Employee.query.get_or_404(user_id)
    return render_template("employee_dashboard.html", employee=employee)
