from Activity25_1 import *
from Activity25_2 import *

tuloy = True

while tuloy:
    print("\n\t*********************************************")
    print("\t     ACTIVITY/CODE CHALLENGE COMPILER      ")
    print("\t*********************************************")
    print("\t\t--- ACTIVITIES ---")
    print("\tA1 - Activity 1")
    print("\tA2 - Activity 2")
    print("\tA3 - Activity 3")
    print("\tA4 - Activity 4")
    print("\tA5 - Activity 5")
    print("\n\t\t--- CODE CHALLENGES ---")
    print("\tC1 - Code Challenge 1")
    print("\tC2 - Code Challenge 2")
    print("\tC3 - Code Challenge 3")
    print("\tC4 - Code Challenge 4")
    print("\n\t0  - Exit")
    print("\t*********************************************")

    ask = input("\tWhich file would you like to run? ").upper()

    if ask == 'A1':
        activity1()
    elif ask == 'A2':
        activity2()
    elif ask == 'A3':
        activity3()
    elif ask == 'A4':
        activity4()
    elif ask == 'A5':
        activity5()
    elif ask == 'C1':
        code_challenge1()
    elif ask == 'C2':
        code_challenge2()
    elif ask == 'C3':
        code_challenge3()
    elif ask == 'C4':
        code_challenge4()
    elif ask == '0':
        tuloy = False
        print("\n\tProgram Ended")
    else:
        print("\n\tInvalid Input! \nPlease choose from the list (ex: A1, C1)")