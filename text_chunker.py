"""
Text Chunker Module

This module provides functionality to chunk text into smaller, more manageable segments based on different criteria such as paragraphs or sentences. This can be particularly useful for text analysis, natural language processing tasks, or preparing text for further processing like summarization or indexing.

The module defines three main functions:
- chunk_by_paragraph: Splits the text into paragraphs using newline characters as delimiters.
- chunk_by_sentences: Splits the text into sentences using a period followed by a space as delimiters.
- chunk_text: Offers a public interface to invoke the chunking functions based on the specified mode (paragraph or sentence).

Examples:
    >>> from text_chunker import chunk_text
    >>> text = "Here is a paragraph. And here is another sentence.\\nNew paragraph here."
    >>> chunk_text(text, 'paragraph')
    ['Here is a paragraph. And here is another sentence.', 'New paragraph here.']
    >>> chunk_text(text, 'sentence')
    ['Here is a paragraph.', 'And here is another sentence.', 'New paragraph here.']
"""

def chunk_by_paragraph(text):
    """
    Chunks text into paragraphs separated by newline characters.

    Args:
        text (str): The text to be chunked.

    Returns:
        list of str: A list where each element is a chunk representing a paragraph.
    """
    return text.split('\n')

def chunk_by_sentences(text):
    """
    Chunks text into sentences using a simple period-based heuristic. This function assumes that each sentence ends with a period followed by a space.

    Args:
        text (str): The text to be chunked.

    Returns:
        list of str: A list where each element is a chunk representing a sentence.
    """
    return text.split('. ')

def chunk_text(text, mode='paragraph'):
    """
    Public interface to chunk text based on the specified mode. Supports chunking by paragraphs or sentences.

    Args:
        text (str): Text to chunk.
        mode (str): Mode of chunking ('paragraph' or 'sentence'), defaults to 'paragraph'.

    Returns:
        list of str: List of chunks, either sentences or paragraphs.

    Raises:
        ValueError: If an unsupported mode is specified.
    """
    if mode == 'paragraph':
        return chunk_by_paragraph(text)
    elif mode == 'sentence':
        return chunk_by_sentences(text)
    else:
        raise ValueError("Unsupported chunking mode specified.")
