
class Start:

    def __init__(self):
        pass

    
    def startMenu(self) -> int :
        print('''
        Welcome to Resume Builder.\n
        1. Build ATS resume
        2. Update your resume 
        ''')

        while True:
            start  = int(input(" > "))

            if start == 1:
                return start
            
            elif start == 2:
                return start
            
            else:
                print("Choose 1 or 2")
                print('''
        1. Build ATS resume
        2. Update your resume
''')



