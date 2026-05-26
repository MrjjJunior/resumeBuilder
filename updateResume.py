
class UpadateResume:
    """
    Class is used to look for Resume in local machine and duplicates the resume to current directory.

    """

    def __init__ (self, resume):
        self.resume = resume


    def readResume(self):
        """
        Reads resume and puts the content of the resume in a List.
        """    
        self.content = []

        try:
            with open(self.resume) as f:
                for line in f:
                    if line == "":
                        continue
                    else:
                        self.content.append(line)
        except FileNotFoundError:
            print("Resume was not file. Make sure it's an absolute path and a txt file")


    def addResumeToRepo(self):
        """
        creates a copy of the resume and puts it into the current directory
        """
        with open("resume.txt", "w") as file:
            file.write("")

        with open("resume.txt", "a") as file:
            for line in self.content:
                if line == "":
                    file.write('\n')
                else:
                    file.write(line)
        


