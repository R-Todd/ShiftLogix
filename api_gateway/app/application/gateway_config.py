# File: api_gateway/app/application/gateway_config.py
# Purpose: Centralized config for all downstream microservice URLs

import os

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service:5001")
CLOCK_SERVICE_URL = os.getenv("CLOCK_SERVICE_URL", "http://clock-service:5002")
SCHEDULE_SERVICE_URL = os.getenv("SCHEDULE_SERVICE_URL", "http://schedule-service:5003")
