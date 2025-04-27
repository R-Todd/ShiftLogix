from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from app.models.employee import Employee

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    email    = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    if not email or not password:
        flash("Email and password are required.", "danger")
        return redirect(url_for("auth.login"))

    user = Employee.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        flash("Invalid credentials. Please try again.", "danger")
        return redirect(url_for("auth.login"))

    token = create_access_token(identity=str(user.userId))
    resp  = redirect(url_for("home.dashboard"))
    set_access_cookies(resp, token)
    return resp

@auth_bp.route("/logout")
def logout():
    resp = redirect(url_for("home.landing"))  # <- go back to public home
    unset_jwt_cookies(resp)
    return resp
