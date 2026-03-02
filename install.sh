#!/bin/bash
echo "🔄 Mise à jour Termux..."
pkg update -y && pkg upgrade -y
echo "📦 Installation Python et pip..."
pkg install python -y
echo "📦 Installation dépendances Python..."
pip install -r requirements.txt
echo "✅ Installation terminée"
