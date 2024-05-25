import pdfplumber
import os
import argparse
import sys


"""
pdf_extractor.py

This script processes a directory of PDF files, extracting text from each file and saving it as a text file in a specified output directory.

Prerequisites:
    - Python 3.6 or above
    - pdfplumber library installed (`pip install pdfplumber`)

Example Usage:
    python pdf_extractor.py --books_dir [path_to_books] --output_dir [path_to_output]

Troubleshooting:
    - If you receive an error stating that the 'books' or 'output' directory does not exist, please check that you have correctly created these directories in your specified paths.
    - Ensure that the paths provided are absolute or relative to the location from which you are running the script.
    - Ensure that all files in the 'books' directory are valid PDF files. The script will not process other file types correctly.
    - If a PDF file cannot be read, verify that it is not corrupted and is accessible.
    - Ensure you are using the correct command-line arguments. Refer to the script's help by running `python pdf_extractor.py --help` for details on how to use the available options.

Parameters:
    --books_dir : Specifies the directory containing the PDF files to be processed. Default is 'books'.
    --output_dir : Specifies the directory where extracted text files should be saved. Default is 'output'.
"""


def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a given PDF file.

    Args:
    pdf_path (str): The file path to the PDF from which to extract text.

    Returns:
    str: The extracted text.
    """

    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # Check if text is found in the page
                text += page_text + '\n'  # Append text from each page with a newline
    return text

def save_text(output_path, text):
    """
    Save a given text to a specified file path.

    Parameters:
    output_path (str): The file path where the text will be saved.
    text (str): Text to be saved.
    """
    with open(output_path, 'w') as f:
        f.write(text)

def process_pdfs(books_dir, output_dir):
    """
    Process each PDF in a specified directory, extract text, and save it to a given output directory.

    Parameters:
    books_dir (str): Directory containing PDF files to process.
    output_dir (str): Directory where extracted text files will be saved.
    """
    for filename in os.listdir(books_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(books_dir, filename)
            extracted_text = extract_text_from_pdf(pdf_path)

            output_filename = filename.replace('.pdf', '.txt')
            output_path = os.path.join(output_dir, output_filename)
            save_text(output_path, extracted_text)
            print(f"Extracted and saved text from {filename} to {output_filename}")


def parse_arguments(args):
    """Parse command line arguments.

    Args:
        args (list of str): Arguments from the command line.

    Returns:
        Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Process PDF files to extract text.")
    parser.add_argument('--books_dir', type=str, default='books',
                        help='Directory containing PDF files')
    parser.add_argument('--output_dir', type=str, default='output',
                        help='Directory to save extracted text files')
    return parser.parse_args(args)


def check_directory_exists(directory):
    """Check if a directory exists, and if not, notify the user."""
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist. Please create it and try again.")
        return False
    return True

def main(books_dir, output_dir):
    """Main function to process PDFs based on specified directories.

    Args:
        books_dir (str): Directory containing PDF files.
        output_dir (str): Directory to save extracted text files.
    """
    if books_dir is None or output_dir is None:
        print("You did not provide one or more directory paths.")
        books_dir = input("Please enter the path to the PDF files: ") if books_dir is None else books_dir
        output_dir = input("Please enter the path to save the output files: ") if output_dir is None else output_dir
    
    if not check_directory_exists(books_dir) or not check_directory_exists(output_dir):
        sys.exit(1)

    process_pdfs(books_dir, output_dir)



if __name__ == "__main__":
    args = parse_arguments(sys.argv[1:])  # sys.argv[1:] ignores the script name in argv[0]
    main(args.books_dir, args.output_dir)

