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
```

## Getting Started

### Prerequisites

- Python 3.7+  
- pip (or venv)  

### Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-org/ShiftLogix.git
   cd ShiftLogix
   ```

   ## (Optional) Create & activate a virtualenv
    
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

   ## Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

   ## Database Migrations
  
   ### Generate a migration after model changes
   ```bash
   python -m flask db migrate -m "Describe change"
   ```
   ### Apply migrations
   ```bash
   python -m flask db upgrade
   ```
   ## Running the App
   ### Set environment variables (optional)
   ```bash
   export FLASK_APP=run.py
   export FLASK_ENV=development
   ```

   ### Start the server
   ```bash
   python run.py
   ```

   Open your browser at `http://127.0.0.1:5000/`
  
   ---
  
   ## Usage
  
   - **Register** a new employee at `/register`
   - **Log in** at `/login`
   - **Clock In/Out** at `/clock`
   - **View or Add Shifts** at `/schedule`
   - **Set Availability** at `/availability`
  
   ---
  
   ## Contributing
  
   Contributions are welcome! Please open an issue or submit a pull request:
  
   1. **Fork** the repository  
   2. **Create** a feature branch  
      ```bash
      git checkout -b feature/XXX
      ```
   ### Commit your changes
   ```bash
   git commit -m "Add XXX feature"
   ```
   
   ### Push
   ```bash
   git push origin feature/XXX
   ```
   
### Open a Pull Request

1. Navigate to your fork on GitHub.  
2. Click the **Compare & pull request** button.  
3. Fill in the title and description.  
4. Click **Create pull request**.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.  
