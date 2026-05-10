from start import Start
from atsResumeBuilder import ATSResume
from updateResume import UpadateResume
import os 


def main():
    start = Start()
    selection = start.startMenu()

    if selection == 1:

        ats = ATSResume("./resume.txt")
        ats.readResume()
        ats.makeATSResume()
        ats.writeToFile()

    elif selection == 2:
        print("Make sure your resume is in docx or txt format\n" \
        "input the absolute path")


        path = input("\nPath: ")
        
        uploadResume = UpadateResume(path)
        
        uploadResume.readResume()
        uploadResume.addResumeToRepo()

if __name__ == "__main__":
    main()
