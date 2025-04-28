"""
File: auth_service/app/presentation/auth_routes.py
Purpose: Defines authentication-related routes, delegating business logic to AuthService.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    set_access_cookies,
    get_jwt_identity,
    jwt_required
)
from app.application.auth_service import AuthService

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

# Instantiate service
auth_service = AuthService()

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() if request.is_json else request.form

    try:
        user_id = auth_service.register_user(data)
        return jsonify({"success": True, "user_id": user_id}), 201
    except ValueError as e:
        return jsonify({"success": False, "message": str(e)}), 400

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() if request.is_json else request.form

    try:
        access_token = auth_service.login_user(data)
        response = jsonify({"access_token": access_token})
        set_access_cookies(response, access_token)
        return response, 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 401

@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()

    try:
        user_info = auth_service.get_current_user(user_id)
        return jsonify(user_info), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
