#!/bin/sh

# wait-for-db.sh
# Purpose: Wait for the MySQL database container to be ready before starting Flask.

echo "||| Waiting for MySQL at $MYSQL_HOST... |||"

# Poll MySQL port 3306 until it's reachable
while ! nc -z "$MYSQL_HOST" 3306; do
  sleep 1
done

echo "|||-------- MySQL is up - starting Flask app...-----------|||"
exec "$@"
