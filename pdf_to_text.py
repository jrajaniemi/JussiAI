#!/usr/bin/env python3

import argparse
from PyPDF2 import PdfReader

def main():
    parser = argparse.ArgumentParser(description='Muuntaa PDF-tiedoston tekstitiedostoksi.')
    parser.add_argument('--import-file', type=str, required=True, help='Polku PDF-tiedostoon, joka halutaan muuntaa.')

    args = parser.parse_args()
    pdf_path = args.import_file
    txt_path = pdf_path.replace('.pdf', '.txt')

    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            with open(txt_path, 'w', encoding='utf-8') as output_file:
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    cleaned_text = ' '.join(text.split())
                    output_file.write(cleaned_text)
        print(f'Tiedosto on tallennettu onnistuneesti: {txt_path}')
    except Exception as e:
        print(f'Virhe tiedostoa käsiteltäessä: {e}')

if __name__ == '__main__':
    main()

