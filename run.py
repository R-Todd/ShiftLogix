"""
File: ShiftLogix/run.py
Purpose: Entry point for the ShiftLogix Flask application.
"""

import os
from backend.app import create_app  # Import the Flask application factory function

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    # Ensure the application runs with the correct settings
    host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")  # Default to localhost
    port = int(os.getenv("FLASK_RUN_PORT", 5000))  # Default to port 5000

    # Run the Flask development server
    print(f"Starting ShiftLogix on http://{host}:{port}")  # Debugging info
    app.run(debug=True, host=host, port=port)
