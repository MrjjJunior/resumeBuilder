from docx import Document

def texToDocx(txt :str) -> Document:
    document = Document()

    with open(txt) as file:
        for line in file:
            document.add_paragraph(line)

    return document


