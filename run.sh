#!/usr/bin/env bash
set -e

# Create virtual environment if needed
if [ ! -d .venv ]; then
    python3 -m venv .venv
fi

# Activate environment and install dependencies
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# Ensure upload directory exists
mkdir -p userfiles

echo "Starting HomeServer on 0.0.0.0:8080"
exec gunicorn --bind 0.0.0.0:8080 server:app
