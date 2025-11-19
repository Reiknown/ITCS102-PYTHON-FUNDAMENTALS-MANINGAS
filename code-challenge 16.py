import os

os.system('cls')
print("STUDENT INFORMATION SYSTEM ")
print("----------------------------------------------\n")


# empty dictionary
student_records = {}

while True:
    print("SELECT FROM THE OPTIONS BELOW \n A- Add Information \n B- Print All Record \n C- Search Student Record \n D- Delete a Student Record \n E- Edit Sutdnet Record \n F- Export Data \n G- Exit")
    choice = input("Your choice            ->   ").lower()
    
    if choice == 'a':
        os.system('cls')
        print("ADDING STUDENT INFORMATION")
        print(" ----------------------------------------------- ")
        student_id = input("Key Search For This Student  use this pattern(course-IDNO) --> ")

        first_name = input("Input student first name --> ").upper()
        last_name = input("Input student last name --> ").upper()
        course = input("Input student course --> ").upper()
        email = input("Input student email address --> ")
        isSingle = input("Are your single? (True or False): ")

        # adding record to our dictionary
        student_records[student_id] = [first_name, last_name, course, email, isSingle ]
        print("DATA SAVED")
        continue

# search
    elif choice == 'b':
        print("PRINTING STUDENT RECORD")

        for id, record in student_records.items():
            print(f"STUDENT ID {id} in STUDENT RECORD {record}")
        continue

    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD ")
        print(" ============================= ")

        search_id = input("Input ID to search ---> ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("====================================")
                print("\n\nRECORD FOUND")
                print("====================================")
                # print the record of search stduent
                for i in student_records[search_id]:
                    print(f"-- {i}")
            else:
                print("====================================")
                print("\n\nNO RECORD FOUND")
                print("====================================")

        continue
    elif choice == 'd':
        os.system('cls')
        print("DELETE EXISTING RECORD")

        search_id = input("Input ID to search ---> ").lower()
        if search_id in student_records.keys():
                print("====================================")
                print("\n\nRECORD FOUND")
                print("====================================")
                # print the record of search stduent
                for i in student_records[search_id]:
                    print(f"-- {i}")

                student_records.pop(search_id)
                print("RECORD DELETED")
        else:
                print("====================================")
                print("\n\nNO RECORD FOUND")
                print("====================================")
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