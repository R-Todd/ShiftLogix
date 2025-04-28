# File: api_gateway/app/presentation/auth_proxy.py
# Purpose: Proxies /api/auth/* to auth_service

from flask import Blueprint, request, redirect, make_response
import requests
import os

auth_bp = Blueprint("auth_proxy", __name__, url_prefix="/api/auth")
AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service:5001")

@auth_bp.route("/register", methods=["POST"])
def register():
    payload = {
        "first_name": request.form.get("first_name"),
        "last_name": request.form.get("last_name"),
        "email": request.form.get("email"),
        "password": request.form.get("password"),
    }
    res = requests.post(f"{AUTH_SERVICE_URL}/api/auth/register", json=payload)

    if res.status_code == 201:
        return redirect("/login")
    return res.json(), res.status_code

@auth_bp.route("/login", methods=["POST"])
def login():
    payload = {
        "email": request.form.get("email"),
        "password": request.form.get("password")
    }
    res = requests.post(f"{AUTH_SERVICE_URL}/api/auth/login", json=payload)

    if res.status_code == 200:
        token = res.json().get("access_token")
        response = redirect("/dashboard")
        response.set_cookie("access_token", token, httponly=True, path="/")
        return response

    return redirect("/login")

def get_current_user():
    token = request.cookies.get("access_token")
    if not token:
        return None

    headers = {"Authorization": f"Bearer {token}"}
    try:
        res = requests.get(f"{AUTH_SERVICE_URL}/api/auth/me", headers=headers)
        if res.status_code == 200:
            return res.json()
    except Exception as e:
        print(f"❌ Error fetching user info: {e}")
    return None
