from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.employee import Employee
from app import db

register_bp = Blueprint("register", __name__, url_prefix="/register")

@register_bp.route("/", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    # Grab first/last name and combine into a single 'name'
    first = request.form.get("first_name", "").strip()
    last  = request.form.get("last_name", "").strip()
    name  = f"{first} {last}".strip()

    # Grab the rest of the fields
    email    = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    # Validate presence
    if not first or not last or not email or not password:
        flash("All fields (first name, last name, email, password) are required.", "danger")
        return redirect(url_for("register.register"))

    # Check for existing email
    if Employee.query.filter_by(email=email).first():
        flash("That email is already registered.", "warning")
        return redirect(url_for("register.register"))

    # Create the user
    user = Employee(name=name, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    flash("Registration successful—please log in.", "success")
    return redirect(url_for("auth.login"))
