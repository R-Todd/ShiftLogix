# File: api_gateway/app/presentation/schedule_proxy.py
# Purpose: Proxies /api/schedule/* to schedule_service



from flask import Blueprint, request, jsonify
import requests
from app.application.jwt_handler import jwt_required_gateway
from app.application.gateway_config import SCHEDULE_SERVICE_URL

schedule_bp = Blueprint("schedule_proxy", __name__, url_prefix="/api/schedule")

@schedule_bp.route("/shifts", methods=["GET"])
@jwt_required_gateway()
def get_shifts():
    res = requests.get(f"{SCHEDULE_SERVICE_URL}/schedule/shifts", headers=request.headers)
    return jsonify(res.json()), res.status_code

@schedule_bp.route("/request", methods=["POST"])
@jwt_required_gateway()
def request_shift_change():
    res = requests.post(
        f"{SCHEDULE_SERVICE_URL}/schedule/request",
        json=request.get_json(),
        headers=request.headers
    )
    return jsonify(res.json()), res.status_code
