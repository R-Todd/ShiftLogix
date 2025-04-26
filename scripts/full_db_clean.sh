#!/bin/bash

# ==============================================================
# ShiftLogix Full Cleanup Script (Bash Version)
# ==============================================================

echo "🚀 Starting ShiftLogix full cleanup..."

# Step 1: Stop and remove containers
docker-compose down

# Step 2: Remove all stopped containers
docker container prune -f

# Step 3: Remove unused images
docker image prune -f

# Step 4: Remove all Docker volumes (⚠️ deletes MySQL DBs)
docker volume prune -f

echo "✅ Cleanup complete! You can now rebuild with 'docker-compose up --build'."
