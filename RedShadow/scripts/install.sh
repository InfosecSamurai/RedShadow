#!/bin/bash

echo "Installing RedShadow dependencies..."
sudo apt update && sudo apt install -y python3 python3-pip python3-venv nmap sqlmap tor

echo "Creating virtual environment..."
python3 -m venv env

# Detect shell and activate the virtual environment correctly
if [ -n "$BASH_VERSION" ]; then
    source env/bin/activate
elif [ -n "$ZSH_VERSION" ]; then
    source env/bin/activate
elif [ -n "$FISH_VERSION" ]; then
    source env/bin/activate.fish
else
    echo "Unknown shell. Please activate the virtual environment manually."
fi

echo "Installing required Python modules..."
pip install -r requirements.txt

echo "Installation complete. Run 'source env/bin/activate' and 'python3 redshadow.py' to start."
