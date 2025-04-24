# File: api_gateway/Dockerfile

FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy everything into container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose gateway port
EXPOSE 8080

# Run the gateway
CMD ["python", "run.py"]
