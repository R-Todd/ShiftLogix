from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_jwt_extended import set_access_cookies, unset_jwt_cookies


def create_auth_blueprint(auth_service):
    bp = Blueprint("auth", __name__)

    @bp.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "GET":
            return render_template("login.html")
        email    = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        try:
            token = auth_service.authenticate(email, password)
        except ValueError:
            flash("Invalid credentials", "danger")
            return redirect(url_for("auth.login"))
        resp = redirect(url_for("employee_dashboard.dashboard"))
        set_access_cookies(resp, token)
        return resp

    @bp.route("/logout")
    def logout():
        resp = redirect(url_for("home.landing"))
        unset_jwt_cookies(resp)
        return resp

    return bp