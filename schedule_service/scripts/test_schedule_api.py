import requests

BASE_URL = "http://localhost:8080/api"
AUTH_URL = "http://localhost:8080/api/auth/login"

# Log in to get token
r = requests.post(AUTH_URL, json={"email": "test_user@example.com", "password": "TestPass123"})
token = r.json().get("access_token")
headers = {"Authorization": f"Bearer {token}"}

# Submit availability
print("📅 Submitting availability...")
r = requests.post(f"{BASE_URL}/availability", json={
    "day_of_week": "Monday",
    "start_time": "09:00",
    "end_time": "17:00"
}, headers=headers)
print("✅ Availability response:", r.status_code, r.json())

# Get availability
print("\n📋 Getting availability...")
r = requests.get(f"{BASE_URL}/availability", headers=headers)
print("✅ Availability list:", r.status_code, r.json())

# Request a shift change
print("\n🔁 Submitting shift change request...")
r = requests.post(f"{BASE_URL}/schedule/request", json={
    "request_type": "add",
    "shift_date": "2025-03-25",
    "start_time": "09:00",
    "end_time": "17:00"
}, headers=headers)
print("✅ Shift change response:", r.status_code, r.json())

# Get shifts
print("\n📆 Getting assigned shifts...")
r = requests.get(f"{BASE_URL}/schedule/shifts", headers=headers)
print("✅ Shifts:", r.status_code, r.json())
