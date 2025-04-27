from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.employee import Employee


def create_employee_dashboard_blueprint(schedule_service):
    bp = Blueprint("employee_dashboard", __name__, url_prefix="/dashboard")

    @bp.route("/")
    @jwt_required()
    def dashboard():
        user_id  = int(get_jwt_identity())
        employee = Employee.query.get_or_404(user_id)
        shifts   = schedule_service.list_for(user_id)
        return render_template("employee_dashboard.html", employee=employee, total_hours=len(shifts))

    return bp