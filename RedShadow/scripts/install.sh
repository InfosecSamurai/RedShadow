#!/bin/bash

echo "Installing RedShadow dependencies..."
sudo apt update && sudo apt install -y python3 python3-pip nmap sqlmap tor

echo "Creating virtual environment..."
python3 -m venv env
source env/bin/activate

echo "Installing required Python modules..."
pip install -r requirements.txt

echo "Installation complete. Run 'python3 redshadow.py' to start."