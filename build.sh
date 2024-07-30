#!/bin/bash
set -e

# Install dependencies
python3 -m pip install -r requirements.txt

# Print the version for debugging
python3 --version

# Run migrations (optional, should be done post-deployment)
python3 manage.py makemigrations
python3 manage.py migrate
g