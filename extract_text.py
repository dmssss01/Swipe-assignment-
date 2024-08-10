from pypdf import PdfReader


def extract_text_from_pdf(path):
    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        page = reader.pages[0]
        text += page.extract_text()

    return text
