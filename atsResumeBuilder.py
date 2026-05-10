
from openai import OpenAI
from pathlib import Path
import os
import sys



class ATSResume:

    def __init__(self, resume):
        self.resume = Path(resume)


    def readResume(self):
        self.content_of_resume = ""
        with open(self.resume, "r") as file:
            for line in file:
                self.content_of_resume += line + "\n"


    def makeATSResume(self):
        client = OpenAI(
        api_key=os.environ.get("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        )

        prompt = f"Take a look at this resume {self.content_of_resume}, make improve it and make it ATS friendly. JUST RESPOND WITH THE REUSME"

        response = client.responses.create(
            input=prompt,
            model="openai/gpt-oss-20b",
        )
        self.newResume = response.output_text

    def writeToFile(self):
        with open("atsResume.txt", "a") as file:
            for line in self.newResume:
                file.writelines(line)





