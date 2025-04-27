from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import (
    create_access_token,
    set_access_cookies,
    get_jwt_identity,
    jwt_required
)
from datetime import timedelta
from app import db
from app.persistence.models import Employee, bcrypt #updated for /persistence/models.py
from app.validators.log_in_validator import validate_log_in
from app.validators.validate_register import validate_register

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() if request.is_json else request.form

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    password = data.get("password")

    valid, message = validate_register(first_name, last_name, email, password)
    if not valid:
        return jsonify({"success": False, "message": message}), 400

    if Employee.query.filter_by(email=email).first():
        return jsonify({"success": False, "message": "Email already registered."}), 409

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = Employee(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password_hash=hashed_password,
        role="Employee"
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": True, "message": "Registration successful!"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() if request.is_json else request.form

    email = data.get("email")
    password = data.get("password")

    valid, message = validate_log_in(email, password)
    if not valid:
        return jsonify({"message": message}), 400

    user = Employee.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid credentials."}), 401

    access_token = create_access_token(identity=str(user.userId), expires_delta=timedelta(hours=1))
    response = jsonify({"access_token": access_token})
    set_access_cookies(response, access_token)
    return response, 200

@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()
    user = Employee.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found."}), 404

    return jsonify({
        "userId": user.userId,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "role": user.role
    }), 200
