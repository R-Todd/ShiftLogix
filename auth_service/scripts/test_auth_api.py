import requests

BASE_URL = "http://localhost:5001/api/auth"

# Test credentials
email = "test_user@example.com"
password = "TestPass123"
first_name = "Test"
last_name = "User"

# Register user
print("🔐 Registering user...")
r = requests.post(f"{BASE_URL}/register", json={
    "first_name": first_name,
    "last_name": last_name,
    "email": email,
    "password": password
})
print("✅ Register response:", r.status_code, r.json())

# Log in
print("\n🔓 Logging in...")
r = requests.post(f"{BASE_URL}/login", json={
    "email": email,
    "password": password
})
print("✅ Login response:", r.status_code, r.json())

# Extract JWT
token = r.json().get("access_token")
headers = {"Authorization": f"Bearer {token}"}

# Get current user
print("\n🙋 Getting user info with JWT...")
r = requests.get(f"{BASE_URL}/me", headers=headers)
print("✅ /me response:", r.status_code, r.json())
