# ShiftLogix — Hexagonal (Ports & Adapters) Edition

All‑in‑one employee shift‑management system built with **Python 3 / Flask** and refactored to a clean _Hexagonal Architecture_.

*   Core business logic lives in framework‑free **services** that depend only on **ports** (interfaces).
   
*   Framework details (Flask, SQLAlchemy, JWT) sit behind **adapters**, so they can be swapped or mocked effortlessly.    

* * *

## ✨ Features

Module  -  What you can do

**Auth**  -  Register • Login • JWT cookie sessions

**Dashboard**  -  Personal overview (hours, shifts)

**Clock**  -  Record start/end times

**Schedule**  -  Add / list shifts

**Availability**  -  Submit availability slots

**Migrations**  -  Alembic for schema versioning

* * *

## 🗂 Project Layout

```
ShiftLogix/
│
├─ run.py                     # tiny runner
├─ requirements.txt
├─ migrations/                # Alembic
└─ app/
   ├─ __init__.py             # app‑factory & wiring
   │
   ├─ ports/                  # ← Hexagon side A (interfaces)
   │   ├─ shift_repository.py
   │   └─ auth_service.py
   │
   ├─ adapters/               # ← Hexagon side B (framework glue)
   │   ├─ sqlalchemy_shift_repo.py
   │   └─ jwt_auth_adapter.py
   │
   ├─ services/               # ← Pure business logic
   │   ├─ schedule_service.py
   │   ├─ clock_service.py
   │   └─ availability_service.py
   │
   ├─ controllers/            # Flask blueprints (driving adapters)
   │   ├─ auth_controller.py
   │   ├─ register_controller.py
   │   ├─ home_controller.py
   │   ├─ employee_dashboard_controller.py
   │   ├─ schedule_controller.py
   │   ├─ clock_controller.py
   │   └─ availability_controller.py
   │
   ├─ models/                 # SQLAlchemy entities
   │   ├─ employee.py
   │   ├─ shift.py
   │   └─ shift_change.py
   │
   ├─ templates/ …            # Jinja2 HTML
   └─ static/ …               # CSS / images
```

* * *

## 🚀 Quick Start

### 1 · Clone & enter

```
git clone https://github.com/your-user/ShiftLogix.git
cd ShiftLogix
```

### 2 · Create & activate a virtual env (optional)

```
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows PowerShell
venv\Scripts\Activate
```

### 3 · Install dependencies

```
pip install -r requirements.txt
```

### 4 · Database migrations

```
# Point Flask to the runner
export FLASK_APP=run.py                 #  PowerShell →  $env:FLASK_APP="run.py"
export FLASK_ENV=development            # enables reload & debug
python -m flask db init                 # once
python -m flask db migrate -m "schema"  # each model change
python -m flask db upgrade              # apply latest
```

### 5 · Run the server

```
python run.py
# → http://127.0.0.1:5000/
```

* * *

## 🏄 How to Use

URL  -  Action

`/register`  -  Create a new employee account

`/login`  -  Sign in (JWT cookie)

`/dashboard`  -  See hours, profile, navigation

`/clock`  -  Clock in / out

`/schedule`  -  Add / view shifts

`/availability`  -  Submit availability requests

* * *

## 🏛 Why Hexagonal?

*   **Framework‑agnostic core** – swap Flask/SQLAlchemy without touching services.
     
*   **Testable** – mock ports to unit‑test pure Python.
     
*   **Composable** – wire different adapters in `app/__init__.py`.     

```
[ Controllers ]  →  [ Services (use‑cases) ]  →  [ Ports ]
        ▲                                         ▼
   Flask / JWT                            SQLAlchemy / JWT
   (driving adapter)                      (driven adapter)
```

* * *

## 🤝 Contributing

1.  **Fork** → `git clone`
     
2.  `git checkout -b feature/xyz`
     
3.  Code + tests → `git commit -m "Add xyz"`
     
4.  `git push origin feature/xyz`
     
5.  Open a **Pull Request** – we ❤️ reviews!
     

* * *

## 📝 License

Released under the **MIT License**
