from docx import Document


class Doc: 

    def __init__(self):
        self.document = Document()

    
    def txt2Doc(self, resume: str) -> Document:
        return self.document