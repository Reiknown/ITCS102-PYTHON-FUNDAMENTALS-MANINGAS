import os

os.system('cls')
print("STUDENT INFORMATION SYSTEM ")
print("----------------------------------------------\n")


# empty dictionary
student_records = {}

while True:
    print("SELECT FROM THE OPTIONS BELOW \n A- Add Information \n B- Search A Record \n C- Delete A Record \n D- Modiy A Record \n P- Print All Data \n E- Exit")

    choice = input("Your choice            ->   ").lower()
    
    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print(" ----------------------------------------------- ")
        search_code = input("Key Search For This Student   --> ")

        first_name = input("Input student first name --> ").upper()
        last_name = input("Input student last name --> ").upper()
        course = input("Input student course --> ").upper()
        email = input("Input student email address --> ")
        isSingle = input("Are your single? (True or False): ")

        student_records = {search_code : [first_name, last_name, course, email, isSingle ]}
        print("DATA SAVED")

        os.system('cls')
        continue

# search
    elif choice == 'b':
        os.system('cls')
        code = input("Input search code ---> ")

        for j in student_records.keys():
            if code in student_records.keys():
                print("RECORD FOUND")

                print('Records')
                print('----------------------------')
                for i in student_records[code]:
                    print(i)

            else:
                    print("NO RECORD FOUND")
        os.system('cls')
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        print("EDITING EXISTING RECORD")
        continue
    elif choice == 'p':
        for i,j in student_records.items():
            print(f"CODE - {i} STORED INFORMATION ---> {j}")
        continue
    elif choice == 'e':
        print("System Exit")
        break
    else:
        print("\nINVALID CHOICE, please RE-ENTER YOUR CHOICE ")
        continue