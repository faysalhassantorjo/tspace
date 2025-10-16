#!/usr/bin/env bash
set -e

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply migrations (SQLite will be created in the container)
python manage.py migrate --no-input
