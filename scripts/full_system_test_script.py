import requests

# ===== CONFIGURATION =====
API_GATEWAY_URL = "http://localhost:8080/api"
EMAIL = "example3@example.com"
PASSWORD = "password3"

# ===== 1. LOGIN AND GET JWT =====
print("\n🔑 [1] Logging in to retrieve JWT...")
login_url = f"{API_GATEWAY_URL}/auth/login"
login_payload = {"email": EMAIL, "password": PASSWORD}

try:
    login_response = requests.post(login_url, json=login_payload)
    print(f"🔎 Status Code: {login_response.status_code}")
    print(f"🔎 Raw Response: {login_response.text}")

    if login_response.status_code == 200:
        access_token = login_response.json().get("access_token")
        if not access_token:
            print("❌ Login succeeded but no access_token found!")
            exit(1)
        print(f"✅ JWT token received.")
    else:
        print(f"❌ Login failed. Cannot continue. Status {login_response.status_code}")
        exit(1)

except Exception as e:
    print(f"❌ Exception during login: {e}")
    exit(1)

headers = {"Authorization": f"Bearer {access_token}"}

# ===== 2. CLOCK IN =====
print("\n⏰ [2] Clocking in...")
clock_in_url = f"{API_GATEWAY_URL}/clock/in"

try:
    clock_in_response = requests.post(clock_in_url, headers=headers)
    if clock_in_response.status_code == 201:
        print("✅ Clock-in successful.")
    else:
        print(f"❌ Clock-in failed. Status {clock_in_response.status_code}: {clock_in_response.text}")
except Exception as e:
    print(f"❌ Exception during clock-in: {e}")

# ===== 3. SUBMIT AVAILABILITY =====
print("\n📅 [3] Submitting availability...")
availability_url = f"{API_GATEWAY_URL}/availability"
availability_payload = {
    "day_of_week": "Monday",
    "start_time": "09:00",
    "end_time": "17:00"
}

try:
    availability_response = requests.post(availability_url, json=availability_payload, headers=headers)
    if availability_response.status_code == 200:
        print("✅ Availability submitted successfully.")
    else:
        print(f"❌ Failed to submit availability. Status {availability_response.status_code}: {availability_response.text}")
except Exception as e:
    print(f"❌ Exception during availability submission: {e}")

# ===== 4. GET AVAILABILITY =====
print("\n📋 [4] Retrieving availability...")
try:
    availability_get_response = requests.get(availability_url, headers=headers)
    if availability_get_response.status_code == 200:
        print("✅ Availability retrieved successfully:")
        print(availability_get_response.json())
    else:
        print(f"❌ Failed to retrieve availability. Status {availability_get_response.status_code}: {availability_get_response.text}")
except Exception as e:
    print(f"❌ Exception during availability retrieval: {e}")

# ===== 5. SUBMIT SHIFT REQUEST =====
print("\n🔁 [5] Submitting shift change request...")
shift_request_url = f"{API_GATEWAY_URL}/schedule/request"
shift_request_payload = {
    "request_type": "add",
    "shift_date": "2025-05-01",  # Example future date
    "start_time": "09:00",
    "end_time": "17:00"
}

try:
    shift_request_response = requests.post(shift_request_url, json=shift_request_payload, headers=headers)
    if shift_request_response.status_code == 200:
        print("✅ Shift change request submitted successfully.")
    else:
        print(f"❌ Failed to submit shift request. Status {shift_request_response.status_code}: {shift_request_response.text}")
except Exception as e:
    print(f"❌ Exception during shift request submission: {e}")

# ===== 6. GET ASSIGNED SHIFTS =====
print("\n📆 [6] Retrieving assigned shifts...")
assigned_shifts_url = f"{API_GATEWAY_URL}/schedule/shifts"

try:
    assigned_shifts_response = requests.get(assigned_shifts_url, headers=headers)
    if assigned_shifts_response.status_code == 200:
        print("✅ Assigned shifts retrieved successfully:")
        print(assigned_shifts_response.json())
    else:
        print(f"❌ Failed to retrieve assigned shifts. Status {assigned_shifts_response.status_code}: {assigned_shifts_response.text}")
except Exception as e:
    print(f"❌ Exception during assigned shifts retrieval: {e}")

# ===== FINAL =====
print("\n✅✅✅ [FINAL] Full system test completed!")
