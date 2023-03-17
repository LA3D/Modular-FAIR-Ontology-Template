#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT_DIR=$(dirname "$SCRIPT_DIR")

# Create a virtual environment
echo "Creating a Python virtual environment..."
python3 -m venv "$ROOT_DIR/venv"

# Activate the virtual environment
echo "Activating the virtual environment..."
source "$ROOT_DIR/venv/bin/activate"

# Install required packages
echo "Installing required packages from requirements.txt..."
pip install -r "$ROOT_DIR/requirements.txt"

echo "Python virtual environment setup is complete."
