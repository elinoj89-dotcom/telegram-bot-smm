#!/bin/bash
echo "Installation du projet SMM..."
pkg update && pkg upgrade -y
pkg install python -y
pip install -r requirements.txt
echo "Installation terminée. Tape 'python main.py' pour lancer."
