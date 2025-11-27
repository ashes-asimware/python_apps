#!/bin/bash
# Startup script to run both Flask and FastAPI

# Start FastAPI in the background
echo "Starting FastAPI on port 8443..."
uv run python imageapi.py &

# Start Flask in the foreground
echo "Starting Flask web app on port 8080..."
uv run python webapp.py
