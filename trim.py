#!/usr/bin/env python3
# Install chmod 755 trim.py
# Usage: ./trim.py --remove_html --replace_newlines --replace_tabs_spaces --remove_urls
import re
import argparse
import sys


def clean_text(
    input_text, remove_html, remove_urls, replace_tabs_spaces, replace_newlines
):
    # Poista HTML-koodi
    if remove_html:
        input_text = re.sub(r"<.*?>", "", input_text)

    # Poista URL:t
    if remove_urls:
        input_text = re.sub(
            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            "",
            input_text,
        )

    # Korvaa tab- ja useat ylimääräiset välilyönnit yhdellä välilyönnillä
    if replace_tabs_spaces:
        input_text = re.sub(r"\s+", " ", input_text)

    # Vaihda rivinvaihtomerkit välilyönneiksi
    if replace_newlines:
        input_text = input_text.replace("\n", " ")

    return input_text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Siivoa tekstiä eri parametreilla.")
    parser.add_argument("--remove_html", action="store_true", help="Poista HTML-koodi")
    parser.add_argument("--remove_urls", action="store_true", help="Poista URL:t")
    parser.add_argument(
        "--replace_tabs_spaces",
        action="store_true",
        help="Korvaa tabit ja ylimääräiset välilyönnit",
    )
    parser.add_argument(
        "--replace_newlines",
        action="store_true",
        help="Korvaa rivinvaihtomerkit välilyönneillä",
    )

    args = parser.parse_args()

    input_text = sys.stdin.read()

    cleaned_text = clean_text(
        input_text,
        args.remove_html,
        args.remove_urls,
        args.replace_tabs_spaces,
        args.replace_newlines,
    )
    print("Puhdistettu teksti:", cleaned_text)
