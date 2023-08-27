#!/usr/bin/env python3
# Jussi.py
from dotenv import load_dotenv
import os
import openai
import sys
import html
import select
import tiktoken

# Function to calculate the number of tokens in a text string


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# Function to create the ~/.jussiai directory if it doesn't exist


def create_jussiai_directory():
    jussiai_dir = os.path.expanduser('~/.jussiai')
    if not os.path.exists(jussiai_dir):
        os.makedirs(jussiai_dir)

# Function to create or overwrite the .env file with the provided API key in the ~/.jussiai directory


def create_env_file(api_key):
    env_path = os.path.expanduser('~/.jussiai/.env')
    with open(env_path, 'w') as env_file:
        env_file.write(f'OPENAI_API_KEY={api_key}')

# Function to load the .env file from the primary path or the current directory


def load_env_file():
    default_path = os.path.expanduser('~/.jussiai/.env')
    if os.path.exists(default_path):
        load_dotenv(dotenv_path=default_path)
        return True
    elif os.path.exists('.env'):
        load_dotenv()
        return True
    else:
        return False

# Function to sanitize user input to include only allowed characters and limit the length


def sanitize_input(input_text, max_length):
    allowed_chars = set(
        '.:-()abcdefghijklmnopqrstuvwxyzåäö ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ')
    sanitized_input = ''.join(
        char for char in input_text if char in allowed_chars)[:max_length]
    sanitized_input = html.escape(sanitized_input)
    return sanitized_input


def main():
    create_jussiai_directory()

    # Attempt to load the .env file
    if not load_env_file():
        # If .env file is not found, prompt the user for the OpenAI API key
        api_key = input("Please provide your OpenAI API key: ")
        create_env_file(api_key)
        print(
            "An .env file with your API key has been created in the ~/.jussiai directory.")

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

    # Calculate the number of tokens in the sanitized input and file content
    num_tokens = num_tokens_from_string(
        sanitized_input + " " + file_content, "cl100k_base")

    # Check if the token limit is exceeded
    if (num_tokens > 40000):
        print("Token limit that was exceeded(" + str(num_tokens) +
              "). You are allowed to use up to 40,000 tokens per minute.")
        return

    # Define the initial messages for the chat
    messages = [
        {"role": "system", "content": "You are a helpful software developer. "},
        {"role": "user", "content": sanitized_input + " " + file_content}
    ]

    try:
        # Set the OpenAI API key
        openai.api_key = os.getenv("OPENAI_API_KEY")

        # Make a request to the OpenAI API
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass
    except openai.error.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass
    except openai.error.RateLimitError as e:
        # Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass

    # Extract and print the assistant's response
    response = completion["choices"][0]["message"]["content"]
    print(response)


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
