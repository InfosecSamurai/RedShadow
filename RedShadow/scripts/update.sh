#!/bin/bash

# Log file for updates
LOG_FILE="update.log"
echo "Starting RedShadow update..." | tee -a "$LOG_FILE"

# Function to log messages
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

# Check if git is installed
if ! command -v git &> /dev/null; then
    log_message "Error: git is not installed. Please install git and try again."
    exit 1
fi

# Ensure we're inside a git repository
if [ ! -d ".git" ]; then
    log_message "Error: No Git repository found. Make sure you're in the RedShadow project directory."
    exit 1
fi

# Fetch updates from the remote repository
log_message "Fetching updates from the remote repository..."
git fetch origin main
if [ $? -ne 0 ]; then
    log_message "Error: Failed to fetch updates from the remote repository."
    exit 1
fi

# Check if there are updates available
LOCAL_COMMIT=$(git rev-parse HEAD)
REMOTE_COMMIT=$(git rev-parse origin/main)

if [ "$LOCAL_COMMIT" = "$REMOTE_COMMIT" ]; then
    log_message "No updates available. RedShadow is already up to date."
    exit 0
fi

# Pull updates from the remote repository
log_message "Pulling updates from the remote repository..."
git pull origin main
if [ $? -ne 0 ]; then
    log_message "Error: Failed to pull updates from the remote repository."
    exit 1
fi

# Install updated dependencies
log_message "Installing updated dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    log_message "Error: Failed to install updated dependencies."
    exit 1
fi

log_message "Update complete. RedShadow is now up to date."