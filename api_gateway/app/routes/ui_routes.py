# File: api_gateway/app/routes/ui_routes.py

import requests
from flask import Blueprint, render_template, request, redirect, make_response, flash, get_flashed_messages
from app.utils.jwt_handler import jwt_required_gateway
from app.gateway_config import AUTH_SERVICE_URL, CLOCK_SERVICE_URL, SCHEDULE_SERVICE_URL

ui_bp = Blueprint("ui_routes", __name__)


def get_user_data(token):
    headers = {"Authorization": f"Bearer {token}"}
    try:
        res = requests.get(f"{AUTH_SERVICE_URL}/api/auth/me", headers=headers)
        if res.ok:
            return res.json()
    except Exception as e:
        print("❌ Error fetching user data:", e)
    return None


@ui_bp.route("/")
def home():
    return render_template("home.html")


@ui_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        payload = {
            "email": request.form["email"],
            "password": request.form["password"]
        }
        res = requests.post(f"{AUTH_SERVICE_URL}/api/auth/login", json=payload)
        if res.ok:
            token = res.json()["access_token"]
            resp = make_response(redirect("/dashboard"))
            resp.set_cookie("access_token", token)
            return resp
        flash("❌ Invalid credentials.", "error")
    return render_template("login.html", messages=get_flashed_messages(with_categories=True))


@ui_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        payload = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": request.form["password"]
        }
        res = requests.post(f"{AUTH_SERVICE_URL}/api/auth/register", json=payload)
        if res.ok:
            flash("✅ Registration successful!", "success")
            return redirect("/login")
        flash("❌ Registration failed.", "error")
    return render_template("register.html", messages=get_flashed_messages(with_categories=True))


@ui_bp.route("/logout")
def logout():
    resp = make_response(redirect("/login"))
    resp.set_cookie("access_token", "", expires=0)
    return resp


@ui_bp.route("/dashboard")
@jwt_required_gateway()
def dashboard():
    token = request.cookies.get("access_token")
    user_data = get_user_data(token)
    return render_template("employee_dashboard.html", employee=user_data)


@ui_bp.route("/clock", methods=["GET", "POST"])
@jwt_required_gateway()
def clock():
    token = request.cookies.get("access_token")
    headers = {"Authorization": f"Bearer {token}"}

    if request.method == "POST":
        action = request.form.get("action")
        url = f"{CLOCK_SERVICE_URL}/api/clock/in" if action == "in" else f"{CLOCK_SERVICE_URL}/api/clock/out"
        try:
            res = requests.post(url, headers=headers)
            try:
                data = res.json()
                msg = data.get("message", "✅ Clock action successful.")
            except ValueError:
                print("⚠ Non-JSON clock service response:", res.text)
                msg = "⚠ Unexpected response from clock service."
            flash(msg, "success" if res.ok else "error")
        except Exception as e:
            print("❌ Clock POST error:", e)
            flash("❌ Failed to clock in/out.", "error")

    return render_template("clock.html", messages=get_flashed_messages(with_categories=True))


@ui_bp.route("/availability", methods=["GET", "POST"])
@jwt_required_gateway()
def availability():
    token = request.cookies.get("access_token")
    headers = {"Authorization": f"Bearer {token}"}
    data = []

    if request.method == "POST":
        payload = {
            "day_of_week": request.form["day_of_week"],
            "start_time": request.form["start_time"],
            "end_time": request.form["end_time"]
        }
        try:
            res = requests.post(f"{SCHEDULE_SERVICE_URL}/availability/", json=payload, headers=headers)
            try:
                msg = res.json().get("message", "✅ Availability submitted.")
            except ValueError:
                print("⚠ Received non-JSON from schedule service:", res.text)
                msg = "❌ Unexpected response from availability service."
            flash(msg, "success" if res.ok else "error")
        except Exception as e:
            print("❌ Availability POST error:", e)
            flash("❌ Failed to submit availability.", "error")

    try:
        res = requests.get(f"{SCHEDULE_SERVICE_URL}/availability/", headers=headers)
        if res.ok:
            data = res.json()
    except Exception as e:
        print("❌ Availability GET error:", e)

    return render_template("availability.html", availabilities=data, messages=get_flashed_messages(with_categories=True))


@ui_bp.route("/schedule", methods=["GET", "POST"])
@jwt_required_gateway()
def schedule():
    token = request.cookies.get("access_token")
    headers = {"Authorization": f"Bearer {token}"}
    shifts = []

    if request.method == "POST":
        payload = {
            "shift_date": request.form.get("shift_date"),
            "start_time": request.form.get("start_time"),
            "end_time": request.form.get("end_time"),
            "request_type": request.form.get("request_type"),
        }
        try:
            res = requests.post(f"{SCHEDULE_SERVICE_URL}/schedule/request", json=payload, headers=headers)
            try:
                msg = res.json().get("message", "✅ Shift request submitted.")
            except ValueError:
                print("⚠ Non-JSON shift response:", res.text)
                msg = "❌ Unexpected response from schedule service."
            flash(msg, "success" if res.ok else "error")
        except Exception as e:
            print("❌ Schedule POST error:", e)
            flash("❌ Failed to submit shift request.", "error")
        return redirect("/schedule")

    try:
        res = requests.get(f"{SCHEDULE_SERVICE_URL}/schedule/shifts", headers=headers)
        if res.ok:
            shifts = res.json()
    except Exception as e:
        print("❌ Schedule GET error:", e)

    return render_template("schedule.html", shifts=shifts, messages=get_flashed_messages(with_categories=True))
