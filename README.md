# Book Advice RAG System


## Text Chunking Module

The Text Chunker module provides functionalities for breaking down text into smaller, more manageable units like paragraphs or sentences. This is particularly useful for subsequent processing in NLP pipelines, data analysis, or any application where text structure plays a crucial role in the processing logic.

### Features

- **Chunk by Paragraphs**: Splits text based on newline characters, useful for documents where paragraphs are well-defined.
- **Chunk by Sentences**: Uses a period-based heuristic to identify sentence boundaries, ideal for processing prose or documents with standard punctuation.

### Installation

No external dependencies are required as this module uses only built-in Python functionality. Ensure you have Python 3.x installed.

### Usage

Import the module and use one of the functions to chunk text as needed:

```python
from text_chunker import chunk_text

# Example text
text = "Welcome to the Text Chunker. This tool is very helpful. Start using it today.\nNew paragraph starts here."

# Get text chunked by sentences
sentence_chunks = chunk_text(text, mode='sentence')
print(sentence_chunks)

# Get text chunked by paragraphs
paragraph_chunks = chunk_text(text)
print(paragraph_chunks)
```


## PDF Text Extractor

The `pdf_extractor.py` script is designed to automate the extraction of text from PDF files stored in a specified directory and save the extracted content as text files in another directory. This tool is especially useful for processing large batches of PDF documents where manual text extraction would be time-consuming and inefficient.

### Features

- **Automated PDF Text Extraction**: Batch process multiple PDFs to extract text.
- **Interactive Mode**: Optionally run the script in an interactive mode that prompts for input paths.
- **Customizable Input/Output Paths**: Configure the directories for source PDFs and output text files via command-line arguments or interactive prompts.

### Prerequisites

Before you run the script, ensure you have the following installed:

- Python 3.6 or higher
- pdfplumber library

You can install the required library using pip:

```bash
pip install pdfplumber
```

### Installation

Download the script from the GitHub repository or clone it using Git:

```bash
git clone https://github.com/yourusername/pdf_extractor.git
```

Navigate to the script directory:

```bash
cd pdf_extractor
```

### Usage

#### Command Line Arguments

To run the script with command-line arguments, specify the paths for input PDF files and output text files as follows:

```bash
python pdf_extractor.py --books_dir path/to/pdf --output_dir path/to/output
```

Replace `path/to/pdf` with the path to your PDF files and `path/to/output` with the path where you want the extracted text files to be saved.

#### Interactive Mode

If you do not specify command-line arguments, the script will prompt you interactively:

```bash
python pdf_extractor.py
```

Follow the on-screen prompts to enter the required paths.

### Configurations

#### Arguments

- `--books_dir`: Specifies the directory containing the PDF files. If not provided, the script will ask for it.
- `--output_dir`: Specifies the directory where the extracted text files should be saved. If not provided, the script will ask for it.

### Troubleshooting

- **Directory Not Found**: Ensure the directories exist as specified or create them before running the script.
- **Permission Denied**: Make sure you have read and write permissions for the directories involved.
- **PDF Processing Errors**: Confirm that all files in the input directory are valid PDFs and not corrupted.


### License

This project is licensed under the Apache 2.0 License.