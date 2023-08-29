#!/usr/bin/env python3
# Shebang specifies that the script should be run using Python 3.
# Comments provide information on how to set permissions and usage.

# Import required modules
import re
import argparse
import sys

# Define the function to clean text
def clean_text(
    input_text, remove_html=True, remove_urls=True, replace_tabs_spaces=True, replace_newlines=True
):
    # Remove HTML tags if remove_html is True
    if remove_html:
        input_text = re.sub(r"<.*?>", "", input_text)

    # Remove URLs if remove_urls is True
    if remove_urls:
        input_text = re.sub(
            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            "",
            input_text,
        )

    # Replace tabs and extra spaces with a single space if replace_tabs_spaces is True
    if replace_tabs_spaces:
        input_text = re.sub(r"\s+", " ", input_text)

    # Replace newline characters with spaces if replace_newlines is True
    if replace_newlines:
        input_text = input_text.replace("\n", " ")

    return input_text

# Main execution starts here
if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Clean text based on various parameters.")
    
    # Define command-line arguments with default values set to True
    parser.add_argument("--remove_html", action="store_true", default=True, help="Remove HTML tags")
    parser.add_argument("--remove_urls", action="store_true", default=True, help="Remove URLs")
    parser.add_argument(
        "--replace_tabs_spaces",
        action="store_true",
        default=True,
        help="Replace tabs and extra spaces with a single space",
    )
    parser.add_argument(
        "--replace_newlines",
        action="store_true",
        default=True,
        help="Replace newline characters with spaces",
    )

    # Parse the arguments
    args = parser.parse_args()

    # Read text from standard input
    input_text = sys.stdin.read()

    # Clean the text based on the arguments
    cleaned_text = clean_text(
        input_text,
        args.remove_html,
        args.remove_urls,
        args.replace_tabs_spaces,
        args.replace_newlines,
    )
    
    # Print the cleaned text
    print(cleaned_text)
