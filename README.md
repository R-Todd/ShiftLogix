# ShiftLogix

**An MVC-structured Flask application for employee shift management**

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Architecture](#architecture)  
- [Folder Structure](#folder-structure)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Database Migrations](#database-migrations)  
  - [Running the App](#running-the-app)  
- [Usage](#usage)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Project Overview

ShiftLogix is an employee shift management system built using the Model-View-Controller (MVC) pattern in Flask. It allows employees to:

- **Clock In/Out** to record working hours.  
- **View and manage schedules**.  
- **Set and update availability**.  
- **Authenticate** via email and password, backed by JWT.

---

## Architecture

We follow a strict MVC separation:

- **Models** (`app/models/`): SQLAlchemy ORM classes (`Employee`, `Shift`, `ShiftChange`).  
- **Views** (`app/templates/`): Jinja2 templates for HTML pages.  
- **Controllers** (`app/controllers/`): Flask Blueprints handling routes, delegating to services.  
- **Services** (`app/services/`): Business logic layer for multi-step workflows (e.g. `ScheduleService`).  
- **Validators** (`app/validators/`): Input validation helpers.  

Extensions used:

- **Flask-SQLAlchemy** for ORM  
- **Flask-Migrate (Alembic)** for migrations  
- **Flask-JWT-Extended** for JWT auth  
- **Flask-Bcrypt** for password hashing

---

## Folder Structure

```text
ShiftLogix/
├─ run.py                  # Application entrypoint
├─ requirements.txt
├─ migrations/             # Database migration scripts
├─ app/
│  ├─ __init__.py          # App factory, extension init, context processors
│  ├─ models/              # ORM models
│  │   ├─ employee.py
│  │   ├─ shift.py
│  │   └─ shift_change.py
│  ├─ controllers/         # Route handlers (Blueprints)
│  │   ├─ auth_controller.py
│  │   ├─ clock_controller.py
│  │   ├─ schedule_controller.py
│  │   ├─ availability_controller.py
│  │   ├─ employee_dashboard_controller.py
│  │   └─ home_controller.py
│  ├─ services/            # Business logic classes
│  ├─ validators/          # Input validation modules
│  ├─ templates/           # Jinja2 templates
│  └─ static/              # CSS, JS, images
└─ tests/                  # Unit and integration tests
