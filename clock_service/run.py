"""
File: clock_service/run.py
Purpose: Entry point for the Clock microservice.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
