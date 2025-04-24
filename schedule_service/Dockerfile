FROM python:3.11-slim

WORKDIR /app

# 🧰 Install netcat-openbsd for wait-for-db.sh
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

COPY . .

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# Make wait-for-db.sh executable
RUN chmod +x wait-for-db.sh

EXPOSE 5003

# Run the Flask app after waiting for the database
CMD ["./wait-for-db.sh", "python", "run.py"]
