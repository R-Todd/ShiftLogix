
# ShiftLogix (Layered Architecture)

This document explains how to set up and run the layered-architecture version of ShiftLogix on a new computer, including environment file templates with explanations.

---

## Prerequisites

- **Git**  
- **Docker & Docker Compose**  
- **Python 3.11 & pip** (optional, if running services manually)

---

## 1. Clone the Repository

```bash
git clone -b layered-architecture https://github.com/R-Todd/ShiftLogix.git
cd ShiftLogix
```

---

## 2. Environment Configuration

Each service (and the API Gateway) uses a `.env` file.  
Below are **templates** with **safe sample values** and **commented explanations**.

You must manually create a `.env` file in each required directory before running the project.

---

### 📂 Root `.env` (ShiftLogix/.env)

```dotenv
# --- MySQL Credentials (used by Docker Compose MySQL containers) ---
MYSQL_USER=sample_user                 # Database username
MYSQL_PASSWORD=sample_password         # Database password
MYSQL_ROOT_PASSWORD=sample_rootpass     # MySQL root account password

# --- Database Names (for each microservice) ---
AUTH_DB_NAME=auth_service_db            # Database for Auth Service
CLOCK_DB_NAME=clock_service_db          # Database for Clock Service
SCHEDULE_DB_NAME=schedule_service_db    # Database for Schedule Service
```

---

### 📂 API Gateway `.env` (ShiftLogix/api_gateway/.env)

```dotenv
# --- JWT Token Secret ---
JWT_SECRET_KEY=sample_jwt_secret        # Secret for verifying JWT tokens (must match Auth Service)

# --- URLs of Microservices (inside Docker Compose network) ---
AUTH_SERVICE_URL=http://auth-service:5001
CLOCK_SERVICE_URL=http://clock-service:5002
SCHEDULE_SERVICE_URL=http://schedule-service:5003
```

---

### 📂 Auth Service `.env` (ShiftLogix/auth_service/.env)

```dotenv
# --- Flask Secret Key ---
SECRET_KEY=sample_flask_secret          # Secret for signing Flask session cookies

# --- JWT Secret Key ---
JWT_SECRET_KEY=sample_jwt_secret         # Secret for generating/verifying JWTs (shared with Gateway)

# --- Database Connection (Auth Service) ---
SQLALCHEMY_DATABASE_URI=mysql+pymysql://sample_user:sample_password@auth-db/auth_service_db
# Format: mysql+pymysql://<username>:<password>@<hostname>/<database>

SQLALCHEMY_TRACK_MODIFICATIONS=False     # Recommended setting to disable event system

# --- MySQL Host (used by wait-for-db.sh script) ---
MYSQL_HOST=auth-db
```

---

### 📂 Clock Service `.env` (ShiftLogix/clock_service/.env)

```dotenv
# --- Flask Secret Key ---
SECRET_KEY=sample_clock_secret          # Secret for signing Flask session cookies

# --- JWT Secret Key ---
JWT_SECRET_KEY=sample_jwt_secret         # Secret for verifying JWTs (shared with Gateway)

# --- Database Connection (Clock Service) ---
SQLALCHEMY_DATABASE_URI=mysql+pymysql://sample_user:sample_password@clock-db/clock_service_db

SQLALCHEMY_TRACK_MODIFICATIONS=False

# --- MySQL Host (used by wait-for-db.sh script) ---
MYSQL_HOST=clock-db
```

---

### 📂 Schedule Service `.env` (ShiftLogix/schedule_service/.env)

```dotenv
# --- Flask Secret Key ---
SECRET_KEY=sample_schedule_secret       # Secret for signing Flask session cookies

# --- JWT Secret Key ---
JWT_SECRET_KEY=sample_jwt_secret         # Secret for verifying JWTs (shared with Gateway)

# --- Database Connection (Schedule Service) ---
SQLALCHEMY_DATABASE_URI=mysql+pymysql://sample_user:sample_password@schedule-db/schedule_service_db

SQLALCHEMY_TRACK_MODIFICATIONS=False

# --- MySQL Host (used by wait-for-db.sh script) ---
MYSQL_HOST=schedule-db
```

---

## 3. Start the Full Stack

After creating all `.env` files:

```bash
docker-compose up --build
```

This will:

- Start MySQL containers (`auth-db`, `clock-db`, `schedule-db`).
- Wait for databases to initialize.
- Start microservices (`auth_service`, `clock_service`, `schedule_service`).
- Start the API Gateway (`api_gateway`) on **http://localhost:8080**.

---

## 4. (Optional) Local Python Setup

You can run services manually without Docker:

```bash
# In each service folder:
pip install -r requirements.txt
python run.py
```

Repeat for:
- `auth_service`
- `clock_service`
- `schedule_service`
- `api_gateway`

---

## 5. Testing Endpoints

Sample scripts to test services:

```bash
bash auth_service/scripts/test_auth.sh
bash clock_service/scripts/test_clock.sh
bash schedule_service/scripts/test_schedule.sh
bash api_gateway/scripts/test_ui.sh
```

---

## Important Notes

- Never commit real `.env` files — use these **templates** instead.
- Always customize secrets and passwords for production environments.
- JWT_SECRET_KEY must match across Auth Service, Clock Service, Schedule Service, and API Gateway.

---

✅ With this, you can safely configure ShiftLogix on any machine without leaking sensitive keys or passwords.
