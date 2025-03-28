import pymupdf as pymu
import pymupdf4llm as pymullm
import textwrap
from langchain_text_splitters import MarkdownHeaderTextSplitter
import os
import sys
import json

def is_valid_markdown_file(file_path):
    """Check if the given path is a valid markdown file."""
    if not file_path.lower().endswith('.md'):
        return False
    if not os.path.isfile(file_path):
        return False
    return True

def split_text_with_splitter(text, **kwargs):
    """Split the given text using MarkdownHeaderTextSplitter."""

    splitter = MarkdownHeaderTextSplitter(**kwargs)
    print("MarkdownHeaderTextSplitter initialized.")
    return splitter.split_text(text)

def split_markdown(apath, **kwargs):
    """Split markdown text or file into headers and text."""
    if is_valid_markdown_file(apath):
        with open(apath, 'r') as file:
            text = file.read()
    if not text:
        raise ValueError("Please provide a valid file path or text to split.")

    if not any(line.startswith('#') for line in text.split('\n')):
        print("The document does not contain a valid header starting with '#'.")
        return ["no headers found"], kwargs['reference']

    return split_text_with_splitter(text, **{k: v for k, v in kwargs.items() if k != 'reference'}), kwargs['reference']

def handle_no_kwargs_no_title(file_name):
    args = {'headers_to_split_on': [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]}
    if '/' in file_name:
        file_name = file_name.split('/')[-1]
    args['reference'] = file_name.split('.')[0]
    return args

def validate_kwargs(kwargs):
    if 'headers_to_split_on' not in kwargs or 'reference' not in kwargs:
        raise ValueError("kwargs must contain 'headers_to_split_on' and 'reference'.")
    if not isinstance(kwargs['reference'], str):
        raise ValueError("'reference' must be a string.")
    if not isinstance(kwargs['headers_to_split_on'], list) or not all(isinstance(item, tuple) for item in kwargs['headers_to_split_on']):
        raise ValueError("'headers_to_split_on' must be a list of tuples.")
    valid_headers = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
    if not any(header in kwargs['headers_to_split_on'] for header in valid_headers):
        raise ValueError("'headers_to_split_on' must contain at least one of the following: [('#', 'Header 1'), ('##', 'Header 2'), ('###', 'Header 3')]")

def process_markdown(input_path, **kwargs):
    """Process a directory or a single markdown file."""
    if kwargs:
        validate_kwargs(kwargs)

    if os.path.isdir(input_path):
        markdown_files = [f for f in os.listdir(input_path) if is_valid_markdown_file(os.path.join(input_path, f))]
        if not markdown_files:
            print("No valid markdown files found in the directory.")
            return
        print(f"Markdown files found: {markdown_files}")
        for md_file in markdown_files:
            if not kwargs:
                kwargs = handle_no_kwargs_no_title(md_file)
            print(f"Using headers to split on: {kwargs['headers_to_split_on']}")
            file_path = os.path.join(input_path, md_file)
            yield from split_markdown(file_path, **kwargs)
    else:
        if not kwargs:
            kwargs = handle_no_kwargs_no_title(input_path)

        yield from split_markdown(input_path, **kwargs)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_markdown.py <markdown_file_or_text> [<kwargs_json>]")
        sys.exit(1)

    input_arg = sys.argv[1]
    kwargs = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}

    result = process_markdown(input_arg, **kwargs)
    for i, element in enumerate(result):
        if i == 0:
            if element[0] == "no headers found":
                print(element[0])
            else:
                print(element[0].metadata)
                print('\n')
                print(element[0].page_content)
        else:
            print('\n')
            print(element)