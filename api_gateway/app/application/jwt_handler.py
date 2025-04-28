# File: api_gateway/app/application/jwt_handler.py
# Purpose: Middleware to validate JWT tokens before proxying requests

import os
import jwt
from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv

#  Load .env file
load_dotenv()

#  Get from environment only — never hardcode
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

if not JWT_SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY is not set in environment")

def jwt_required_gateway():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            token = None

            # Try Authorization header first
            auth_header = request.headers.get("Authorization")
            if auth_header and auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

            # Fallback to secure cookie
            if not token:
                token = request.cookies.get("access_token")

            if not token:
                return jsonify({"msg": "Missing JWT token"}), 401

            try:
                jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
            except jwt.InvalidTokenError:
                return jsonify({"msg": "Invalid JWT token"}), 401

            return fn(*args, **kwargs)
        return wrapper
    return decorator

