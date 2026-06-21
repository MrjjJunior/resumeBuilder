from pypdf import PdfReader
from pypdf import PdfWriter

def readPdf(pdf: str) -> str:
    reader = PdfReader(pdf)

    text = ""

    for page in len(reader.pages):
        text.append(reader.pages[page].extract_text())
    
    return text


async def txtToPdf(txt: str):
    pdf = PdfWriter()

if __name__ == "__main__":
    ...