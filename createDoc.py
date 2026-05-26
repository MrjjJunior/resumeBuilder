from docx import Document


class Doc: 
    """
    Class will create a resume that is in document format.
    """
    def __init__(self):
        self.document = Document()

    
    def txt2Doc(self, resume: str) -> Document:
        """
        Method rconverts resume.txt to a docment format 

        Args: 
            resume (str): Is the resume in txt format.
        Returns:
            Docuent: Will return resume in a document format.
        """
        return self.document