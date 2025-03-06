#!/bin/bash

echo "Updating RedShadow..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Error: git is not installed. Please install git and try again."
    exit 1
fi

# Ensure we're inside a git repository
if [ ! -d ".git" ]; then
    echo "Error: No Git repository found. Make sure you're in the RedShadow project directory."
    exit 1
fi

git pull origin main

echo "Update complete."
