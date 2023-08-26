#!/usr/bin/env python3
# Jussi.py
from dotenv import load_dotenv
import os
import openai
import sys
import html
import select

def create_jussiai_directory():
    # Create the ~/.jussiai directory if it doesn't exist
    jussiai_dir = os.path.expanduser('~/.jussiai')
    if not os.path.exists(jussiai_dir):
        os.makedirs(jussiai_dir)

def create_env_file(api_key):
    # Create or overwrite the .env file with the provided API key in the ~/.jussiai directory
    env_path = os.path.expanduser('~/.jussiai/.env')
    with open(env_path, 'w') as env_file:
        env_file.write(f'OPENAI_API_KEY={api_key}')

def load_env_file():
    # Define the primary path for the .env file
    default_path = os.path.expanduser('~/.jussiai/.env')

    # If the .env file exists in the primary path, load it
    if os.path.exists(default_path):
        load_dotenv(dotenv_path=default_path)
        return True
    # If the .env file exists in the current directory, load it
    elif os.path.exists('.env'):
        load_dotenv()
        return True
    # If the .env file is not found in either location, return False
    else:
        return False

def sanitize_input(input_text, max_length):
    # Sanitize user input to include only allowed characters and limit the length
    allowed_chars = set('.:-()abcdefghijklmnopqrstuvwxyzåäö ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ')
    sanitized_input = ''.join(char for char in input_text if char in allowed_chars)[:max_length]
    sanitized_input = html.escape(sanitized_input)
    return sanitized_input

def main():
    create_jussiai_directory()

    # Attempt to load the .env file
    if not load_env_file():
        # If .env file is not found, prompt the user for the OpenAI API key
        api_key = input("Please provide your OpenAI API key: ")
        create_env_file(api_key)
        print("An .env file with your API key has been created in the ~/.jussiai directory.")

    # Check if the user provided text as a parameter
    if len(sys.argv) < 2:
        print("Please provide text as a parameter!")
        return

    # Add and sanitize the user's input for the messages
    user_input = ' '.join(sys.argv[1:])
    max_length = 100
    sanitized_input = sanitize_input(user_input, max_length)
    file_content = ""

    i, o, e = select.select([sys.stdin], [], [], 0.1)
    if i:
        file_content = sys.stdin.read()

    # print(file_content)

    # Define the initial messages for the chat
    messages=[
        {"role": "system", "content": "You are a helpful software developer. "},
        {"role": "user", "content": sanitized_input + " " +file_content}
    ]
    # print(messages)

    # Set the OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    # Make a request to the OpenAI API
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    # Extract and print the assistant's response
    response = completion["choices"][0]["message"]["content"]
    print(response)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()