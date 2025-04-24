# File: run.py
from dotenv import load_dotenv
load_dotenv()  # ✅ Load .env before app starts

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
