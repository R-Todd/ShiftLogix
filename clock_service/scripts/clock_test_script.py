"""
File: clock_service/scripts/test_clock_api.py
Purpose: Test the clock-in and clock-out endpoints using a valid JWT.
"""

import requests

# URLs
AUTH_URL = "http://localhost:5001/api/auth/login"
CLOCK_URL = "http://localhost:5002/api/clock"

# Test credentials from auth test
credentials = {
    "email": "test_user@example.com",
    "password": "TestPass123"
}

print("🔐 Logging in to auth service...")
login_response = requests.post(AUTH_URL, json=credentials)

if login_response.status_code != 200:
    print("❌ Login failed:", login_response.status_code)
    print(login_response.text)
    exit()

token = login_response.json().get("access_token")
headers = {"Authorization": f"Bearer {token}"}

def safe_json_print(label, response):
    try:
        print(f"✅ {label} {response.status_code}", response.json())
    except Exception:
        print(f"⚠️ {label} {response.status_code} (Non-JSON or error):\n", response.text)

# Clock in
print("\n🕒 Clocking in...")
r = requests.post(f"{CLOCK_URL}/in", headers=headers)
safe_json_print("Clock-in response:", r)

# Clock out
print("\n🕔 Clocking out...")
r = requests.post(f"{CLOCK_URL}/out", headers=headers)
safe_json_print("Clock-out response:", r)
