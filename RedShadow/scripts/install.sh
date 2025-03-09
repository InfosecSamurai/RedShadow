#!/bin/bash

# Log file for installation
LOG_FILE="install.log"
echo "Starting RedShadow installation..." | tee -a "$LOG_FILE"

# Function to log messages
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    log_message "Python 3 is not installed. Installing Python 3..."
    sudo apt update && sudo apt install -y python3
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    log_message "pip3 is not installed. Installing pip3..."
    sudo apt install -y python3-pip
fi

# Check if git is installed
if ! command -v git &> /dev/null; then
    log_message "git is not installed. Installing git..."
    sudo apt install -y git
fi

# Install system dependencies
log_message "Installing system dependencies (nmap, sqlmap, tor)..."
sudo apt update && sudo apt install -y nmap sqlmap tor

# Create virtual environment
log_message "Creating virtual environment..."
python3 -m venv env
if [ $? -ne 0 ]; then
    log_message "Failed to create virtual environment. Exiting."
    exit 1
fi

# Activate virtual environment
log_message "Activating virtual environment..."
if [ -n "$BASH_VERSION" ]; then
    source env/bin/activate
elif [ -n "$ZSH_VERSION" ]; then
    source env/bin/activate
elif [ -n "$FISH_VERSION" ]; then
    source env/bin/activate.fish
else
    log_message "Unknown shell. Please activate the virtual environment manually."
    exit 1
fi

# Install Python dependencies
log_message "Installing required Python modules..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    log_message "Failed to install Python modules. Exiting."
    exit 1
fi

# Create necessary directories
log_message "Creating necessary directories..."
mkdir -p logs reports templates
if [ $? -ne 0 ]; then
    log_message "Failed to create directories. Exiting."
    exit 1
fi

# Initialize the database
log_message "Initializing the database..."
python3 core/database.py
if [ $? -ne 0 ]; then
    log_message "Failed to initialize the database. Exiting."
    exit 1
fi

log_message "Installation complete. Run 'source env/bin/activate' and 'python3 redshadow.py' to start."