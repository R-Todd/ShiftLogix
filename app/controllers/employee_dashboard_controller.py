from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.employee import Employee

employee_dashboard_bp = Blueprint("employee_dashboard", __name__, url_prefix="/dashboard")

@employee_dashboard_bp.route("/")
@jwt_required()
def dashboard():
    user_id = get_jwt_identity()
    user    = Employee.query.get_or_404(user_id)
    return render_template("employee_dashboard.html", user=user)
