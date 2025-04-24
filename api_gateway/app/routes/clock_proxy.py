# File: api_gateway/app/routes/clock_proxy.py
# Purpose: Proxies /api/clock/* to clock_service

from flask import Blueprint, request, redirect, make_response, render_template
import requests
import os

clock_bp = Blueprint("clock_proxy", __name__, url_prefix="/api/clock")
CLOCK_SERVICE_URL = os.getenv("CLOCK_SERVICE_URL", "http://clock-service:5002/api/clock")

@clock_bp.route("/in", methods=["POST"])
def clock_in_proxy():
    token = request.cookies.get("access_token")
    headers = {"Authorization": f"Bearer {token}"}

    res = requests.post(f"{CLOCK_SERVICE_URL}/in", headers=headers)
    data = res.json()
    status = res.status_code

    if "text/html" in request.headers.get("Accept", "") or "application/x-www-form-urlencoded" in request.content_type:
        return render_template("clock.html", message=data.get("message"), success=(status == 200))
    
    return data, status

@clock_bp.route("/out", methods=["POST"])
def clock_out_proxy():
    token = request.cookies.get("access_token")
    headers = {"Authorization": f"Bearer {token}"}

    res = requests.post(f"{CLOCK_SERVICE_URL}/out", headers=headers)
    data = res.json()
    status = res.status_code

    if "text/html" in request.headers.get("Accept", "") or "application/x-www-form-urlencoded" in request.content_type:
        return render_template("clock.html", message=data.get("message"), success=(status == 200))
    
    return data, status
