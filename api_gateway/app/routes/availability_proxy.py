# File: api_gateway/app/routes/availability_proxy.py
# Purpose: Proxies /api/availability/* to availability-related endpoints in schedule_service

# File: api_gateway/app/routes/availability_proxy.py
# Purpose: Proxies /api/availability/* to schedule_service

from flask import Blueprint, request, jsonify
import requests
from app.utils.jwt_handler import jwt_required_gateway
from app.gateway_config import SCHEDULE_SERVICE_URL

availability_bp = Blueprint("availability_proxy", __name__, url_prefix="/api/availability")

@availability_bp.route("/", methods=["GET"])
@jwt_required_gateway()
def get_availability():
    res = requests.get(f"{SCHEDULE_SERVICE_URL}/availability/", headers=request.headers)
    return jsonify(res.json()), res.status_code

@availability_bp.route("/", methods=["POST"])
@jwt_required_gateway()
def post_availability():
    res = requests.post(
        f"{SCHEDULE_SERVICE_URL}/availability/",
        json=request.get_json(),
        headers=request.headers
    )
    return jsonify(res.json()), res.status_code


