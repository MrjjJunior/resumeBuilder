from start import Start
from atsResumeBuilder import ATSResume
from updateResume import UpadateResume
from createDoc import Doc
import os 
import sys

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
            ats.txt2Doc()


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
    main()
