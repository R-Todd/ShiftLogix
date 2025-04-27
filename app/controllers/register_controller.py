from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.models.employee import Employee
from app import db, bcrypt


def create_register_blueprint(auth_service):
    bp = Blueprint("register", __name__, url_prefix="/register")

    @bp.route("/", methods=["GET", "POST"])
    def register():
        if request.method == "GET":
            return render_template("register.html")
        data = request.form
        if Employee.query.filter_by(email=data['email']).first():
            flash("Email already registered", "danger")
            return redirect(url_for('register.register'))
        new_user = Employee(
            name=data['first_name'] + ' ' + data['last_name'],
            email=data['email']
        )
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful—please log in.", "success")
        return redirect(url_for('auth.login'))

    return bp