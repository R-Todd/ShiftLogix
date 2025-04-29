# File: api_gateway/Dockerfile

# 1. Base image
FROM python:3.11-alpine

# 2. Set working directory inside container
WORKDIR /app

# 3. Install OS-level build deps & wget (for healthcheck)
#    - gcc & musl-dev are needed if any package has C extensions
#    - libffi-dev & openssl-dev are often required for cryptography/PyJWT
RUN apk add --no-cache \
      gcc \
      musl-dev \
      libffi-dev \
      openssl-dev \
      wget

# 4. Copy & install Python dependencies (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your source
COPY . .

# 6. Expose the port the app runs on
EXPOSE 8080

# 7. Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
  CMD wget --quiet --tries=1 --spider http://localhost:8080/ || exit 1

# 8. Default command
CMD ["python", "run.py"]

