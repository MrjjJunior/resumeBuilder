import sys

class Start:
    """
    Creates the start menu. App Flow.
    """
    def __init__(self):
        pass

    
    def startMenu(self) -> int :
        """
        Prints Welcome menu
        
        Returns:
            int: 1 to build ats reume, 2 to update resume, 3 to quit program.
        """
        print('''
        Welcome to Resume Builder.\n
        1. Build ATS resume
        2. Update your resume
        3. Exit
        ''')

        while True:
            try:
                start  = int(input("\t> "))

                match start:
                    case 1:
                        return start
                    case 2:
                        return start
                    case 3:
                        return sys.exit()
                    case _:
                        print("Choose 1 or 2")
                        print('''
                        1. Build ATS resume
                        2. Update your resume
                            ''')
            except ValueError:
                print("Input an integer")



