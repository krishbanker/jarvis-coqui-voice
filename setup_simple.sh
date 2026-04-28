#!/bin/bash

# Simple Coqui TTS Setup (No Virtual Environment)
# Direct installation to system Python

echo "🎤 Coqui TTS - Simple Direct Installation"
echo "=========================================="

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Extract major and minor version
IFS='.' read -r major minor patch <<< "$python_version"

if [ "$major" -lt 3 ] || ([ "$major" -eq 3 ] && [ "$minor" -lt 10 ]); then
    echo "❌ Error: Python 3.10 or higher required (you have $python_version)"
    exit 1
fi

echo "✅ Python version check passed"

# Upgrade pip
echo ""
echo "⬆️  Upgrading pip..."
pip install --upgrade pip setuptools wheel

# Install dependencies directly
echo ""
echo "📥 Installing Coqui TTS and dependencies..."
pip install TTS==0.22.0
pip install torch==2.0.1 torchaudio==2.0.2
pip install soundfile==0.12.1
pip install numpy==1.24.3 scipy==1.11.2 librosa==0.10.0

echo ""
echo "✅ Installation complete!"
echo ""
echo "To start the TTS application, run:"
echo "  python3 app.py"
echo ""
echo "Or run the one-liner:"
echo "  python3 app.py"
