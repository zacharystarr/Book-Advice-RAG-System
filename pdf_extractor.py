import pdfplumber

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


if __name__ == "__main__":
    # Example usage
    pdf_file_path = 'books/pdf_file.pdf'
    extracted_text = extract_text_from_pdf(pdf_file_path)
    print(extracted_text)

