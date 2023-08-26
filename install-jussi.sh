#!/bin/bash

# Install required libraries
pip3 install openai python-dotenv

# Copy Jussi to the user's home directory
cp Jussi.py /usr/local/bin/Jussi

# Make Jussi executable
chmod +x /usr/local/bin/Jussi

# Display installation completed message
echo "Jussi has been installed. You can now use it by running Jussi"
