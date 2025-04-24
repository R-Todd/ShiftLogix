import requests

AUTH_URL = "http://localhost:5001/api/auth/login"
CLOCK_URL = "http://localhost:5002/api/clock"

# Change this to an existing user
email = "alice@example.com"
password = "Test123!"

# Step 1: Log in to get access token
print("Logging in...")
auth_response = requests.post(AUTH_URL, json={
    "email": email,
    "password": password
})

if auth_response.status_code != 200:
    print("Login failed:", auth_response.json())
    exit()

access_token = auth_response.json().get("access_token")
headers = {
    "Authorization": f"Bearer {access_token}"
}
print("✅ Logged in!")

# Step 2: Clock in (1st time)
print("\n🕒 Clocking in (first time)...")
response1 = requests.post(f"{CLOCK_URL}/in", headers=headers)
print("Response:", response1.status_code, response1.json())

# Step 3: Clock in (2nd time — without clocking out)
print("\n🕒 Attempting second clock in (should ideally be blocked)...")
response2 = requests.post(f"{CLOCK_URL}/in", headers=headers)
print("Response:", response2.status_code, response2.json())
