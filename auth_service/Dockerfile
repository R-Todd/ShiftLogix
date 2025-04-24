# Use Python 3.10 slim image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# 🧰 Install netcat-openbsd (for wait-for-db.sh to check MySQL readiness)
# The `nc` command is provided by netcat-openbsd in slim Debian-based images
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

# Copy application files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🔓 Make the wait-for-db script executable
RUN chmod +x wait-for-db.sh

# Expose the service port
EXPOSE 5001

# Run the app via wait-for-db to ensure DB is ready
CMD ["./wait-for-db.sh", "python", "run.py"]

