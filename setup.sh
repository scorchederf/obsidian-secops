#!/usr/bin/env bash

# ============================================================
# Simple Python environment setup for secopskb builder
# ============================================================

set -e

echo "[INFO] Starting environment setup..."

# --- Config ---
VENV_DIR=".venv"
PYTHON_BIN="python3"

# --- Check Python ---
if ! command -v $PYTHON_BIN &> /dev/null; then
    echo "[ERROR] python3 not found. Install it first."
    exit 1
fi

# --- Create venv ---
if [ ! -d "$VENV_DIR" ]; then
    echo "[INFO] Creating virtual environment..."
    $PYTHON_BIN -m venv $VENV_DIR
else
    echo "[INFO] Virtual environment already exists."
fi

# --- Activate venv ---
echo "[INFO] Activating virtual environment..."
source $VENV_DIR/bin/activate

# --- Upgrade pip ---
echo "[INFO] Upgrading pip..."
pip install --upgrade pip

# --- Install requirements ---
echo "[INFO] Installing dependencies..."

pip install \
    requests \
    pyyaml

# --- Optional: dev/debug tools ---
# Uncomment if you want them
# pip install black flake8

echo "[INFO] Setup complete."
echo ""
echo "To activate the environment later:"
echo "source $VENV_DIR/bin/activate"
