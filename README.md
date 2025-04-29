
# ShiftLogix (Layered Architecture)

This document explains how to set up and run the layered-architecture version of ShiftLogix on a new computer, including all required environment variable values.

---

## Prerequisites

- **Git**  
- **Docker & Docker Compose**  
- **Python 3.11 & pip** (if you want to run services locally outside Docker)

---

## 1. Clone the Repository

```bash
git clone -b layered-architecture https://github.com/R-Todd/ShiftLogix.git
cd ShiftLogix
```

---

## 2. Environment Configuration

Each service (and the API gateway) uses a `.env` file loaded via `python-dotenv`. Below are the exact values you need in **each** file.

### 2.1 Root `.env` (`ShiftLogix/.env`)

```dotenv
# Shared MySQL credentials
MYSQL_USER=shiftlogix_user
MYSQL_PASSWORD=AdminPassword1234
MYSQL_ROOT_PASSWORD=rootpass

# Database names per microservice
AUTH_DB_NAME=shiftlogix
CLOCK_DB_NAME=clock_service_db
SCHEDULE_DB_NAME=schedule_service_db
```

### 2.2 API Gateway `.env` (`ShiftLogix/api_gateway/.env`)

```dotenv
# JWT key for verifying tokens
JWT_SECRET_KEY=super_secret_abc123

# Downstream service base URLs
AUTH_SERVICE_URL=http://auth-service:5001
CLOCK_SERVICE_URL=http://clock-service:5002
SCHEDULE_SERVICE_URL=http://schedule-service:5003
```

### 2.3 Auth Service `.env` (`ShiftLogix/auth_service/.env`)

```dotenv
# Flask & JWT secrets
SECRET_KEY=xyz123fgb
JWT_SECRET_KEY=super_secret_abc123

# SQLAlchemy connection (auth-db)
SQLALCHEMY_DATABASE_URI=mysql+pymysql://shiftlogix_user:AdminPassword1234@auth-db/shiftlogix
SQLALCHEMY_TRACK_MODIFICATIONS=False

# Host for wait-for-db
MYSQL_HOST=auth-db
```

### 2.4 Clock Service `.env` (`ShiftLogix/clock_service/.env`)

```dotenv
# Flask & JWT secrets
SECRET_KEY=your_clock_secret
JWT_SECRET_KEY=super_secret_abc123

# SQLAlchemy connection (clock-db)
SQLALCHEMY_DATABASE_URI=mysql+pymysql://shiftlogix_user:AdminPassword1234@clock-db/clock_service_db
SQLALCHEMY_TRACK_MODIFICATIONS=False

# Host for wait-for-db
MYSQL_HOST=clock-db
```

### 2.5 Schedule Service `.env` (`ShiftLogix/schedule_service/.env`)

```dotenv
# Flask & JWT secrets
SECRET_KEY=your_schedule_secret
JWT_SECRET_KEY=super_secret_abc123

# SQLAlchemy connection (schedule-db)
SQLALCHEMY_DATABASE_URI=mysql+pymysql://shiftlogix_user:AdminPassword1234@schedule-db/schedule_service_db
SQLALCHEMY_TRACK_MODIFICATIONS=False

# Host for wait-for-db
MYSQL_HOST=schedule-db
```

---

## 3. Start the Full Stack

1. **Ensure Docker Desktop is running.**  
2. From the project root, run:

```bash
docker-compose up --build
```

This will:
- Spin up three MySQL containers (`auth-db`, `clock-db`, `schedule-db`) with named volumes for persistence.
- Wait for each DB via `wait-for-db.sh` before launching its Flask service.
- Build and start the three microservices on ports **5001**, **5002**, **5003**.
- Build and start the API Gateway on port **8080**.

3. **Visit** `http://localhost:8080` to access the ShiftLogix UI/API Gateway.

---

## 4. (Optional) Local Python Setup

If you prefer running services directly in Python (outside Docker):

```bash
# From each service directory
pip install -r requirements.txt
python run.py
```

Repeat for:
- `auth_service/`
- `clock_service/`
- `schedule_service/`
- `api_gateway/`

---

## 5. Testing Endpoints

Quick test scripts are available in each service’s `scripts/` folder. For example:

```bash
bash auth_service/scripts/test_auth.sh
bash clock_service/scripts/test_clock.sh
bash schedule_service/scripts/test_schedule.sh
bash api_gateway/scripts/test_ui.sh
```

These cover registration, login, clock-in/out, availability CRUD, and shift retrieval to verify everything’s wired up correctly.

---

With this in place, you should be able to clone, configure, and spin up the entire ShiftLogix system on any new machine. Enjoy!
