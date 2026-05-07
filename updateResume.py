


class UpadateResume:

    def __init__ (self, resume):
        self.resume = resume

    
    def readResume(self):
        
        self.content = []

        with open(self.resume) as f:
            for line in f:
                if line == "":
                    continue
                else:
                    self.content.append(line)
        
    
    def addResumeToRepo(self):
        with open("resume.txt", "w") as file:
            file.write("")

        with open("resume.txt", "a") as file:
            for line in self.content:
                if line == "":
                    file.write('\n')
                else:
                    file.write(line)
        


