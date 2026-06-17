from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.start import Start
from app.atsResumeBuilder import ATSResume
from app.updateResume import UpadateResume

from pathlib import Path

import os 
import sys
import re


app = FastAPI()
templates = Jinja2Templates(directory="static/templates")

@app.get("/")
def home():
    return {"message": "Home"}

@app.get("/resumes")
def getResumes():
    resumes = Path("resumes")

    cv = {}

    # for date in resumes.iterdir():
    #     print(date)

    for root, dirs, files in os.walk(resumes):
        if root.startswith("resumes/2"):
           for file in files:
               cv[root[8:]] = file
    
    return cv


def main():
    directory_path = "resumes/.logs/"
    if os.path.isdir(directory_path) !=  True:
        os.makedirs(os.path.dirname(directory_path), exist_ok=True)
    
    try:
        start = Start()
        selection = start.startMenu()

        if selection == 1:

            ats = ATSResume("./resume.txt")
            ats.readResume()
            ats.jobListingInfo()
            ats.makeATSResume()
            ats.writeToFile()


        elif selection == 2:
            print("Make sure your resume is in docx or txt format\n" \
            "input the absolute path")


            path = input("\nPath: ")
            
            uploadResume = UpadateResume(path)
            
            uploadResume.readResume()
            uploadResume.addResumeToRepo()
            main()
    except KeyboardInterrupt:
        sys.exit("Goodbye and good luck on your journey ;)")        



if __name__ == "__main__":
    #main()
    getResumes()
