import pymupdf as pymu
import pymupdf4llm as pymullm
import os
import sys




def extract_text_from_pdf(file_name):
    """Use pymupdf to extract text from a PDF file."""
    if not file_name.lower().endswith('.pdf'):
        raise ValueError("The file provided is not a PDF.")
    try:
        an_opened_pdf = pymu.open(file_name)
        text = ''
        for page in an_opened_pdf:
            text += page.get_text() + '\n\n'
        return text
    except Exception as e:
        raise RuntimeError(f"An error occurred while extracting text from the PDF: {e}")

def extract_markdown_from_pdf(file_name):
    """Use pymupdf4llm to extract markdown from a PDF file."""
    if not file_name.lower().endswith('.pdf'):
        raise ValueError("The file provided is not a PDF.")
    try:
        an_opened_pdf = pymullm.to_markdown(file_name)
        # print(an_opened_pdf)
        return an_opened_pdf
    except Exception as e:
        raise RuntimeError(f"An error occurred while extracting markdown from the PDF: {e}")


def process_pdf_directory(directory, output_directory, extract_method='markdown'):
    """Process all PDF files in a directory using the specified extraction method."""
    if not os.path.isdir(directory):
        # print(directory)
        raise ValueError("The provided path is not a directory.")

    if not os.path.isdir(output_directory):
        os.makedirs(output_directory)

    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    print(f"PDF files found: {pdf_files}")
    for pdf_file in pdf_files:
        file_path = os.path.join(directory, pdf_file)
        output_path = os.path.join(output_directory, os.path.splitext(pdf_file)[0] + '.md')
        if extract_method == 'text':
            with open(output_path, 'w') as output_file:
                output_file.write(extract_text_from_pdf(file_path))
        else:
            with open(output_path, 'w') as output_file:
                output_file.write(extract_markdown_from_pdf(file_path))
        yield output_path

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python pdf_to_markdown.py <pdf_directory> <output_directory> [extract_method]")
        sys.exit(1)

    input_arg = sys.argv[1]
    output_arg = sys.argv[2]
    extract_method = sys.argv[3] if len(sys.argv) > 3 else 'markdown'

    result = process_pdf_directory(input_arg, output_arg, extract_method)
    for i, element in enumerate(result):
       print(f"Output file saved to: {element}")

