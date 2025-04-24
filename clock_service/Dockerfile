# Use Python 3.11 slim image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# 🧰 Install netcat-openbsd for wait-for-db.sh
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

# Copy application source into container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🔓 Make the wait script executable
RUN chmod +x wait-for-db.sh

# Expose Flask port
EXPOSE 5002

# Run the app with wait-for-db to ensure DB readiness
CMD ["./wait-for-db.sh", "python", "run.py"]

