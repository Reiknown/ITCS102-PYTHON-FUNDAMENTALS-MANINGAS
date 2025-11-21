import os
import json

os.system('cls')
print("STUDENT INFORMATION SYSTEM ")
print("----------------------------------------------\n")


# empty dictionary
student_records = {}

while True:
    print("SELECT FROM THE OPTIONS BELOW \n A- Add Information \n B- Print All Record \n C- Search Student Record \n D- Delete a Student Record \n E- Edit / Modify Student Record \n F- Export Student Recrod \n G- Import Student Record \n\n X - Exit")
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

        # adding record to our dictionary
        student_records[student_id] = [first_name, last_name, course, email]
        print("DATA SAVED")
        continue

# search
    elif choice == 'b':
        os.system('cls')
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
            break
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

    elif choice == 'e':
        os.system('cls')
        print(" STUDENT RECORD ")
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

                first_name = input("Input NEW student first name --> ").upper()
                last_name = input("Input NEW student last name --> ").upper()
                course = input("Input NEW student course --> ").upper()
                email = input("Input NEW student email address --> ")

                student_records[search_id][0] = first_name
                student_records[search_id][1] = last_name
                student_records[search_id][2] = course
                student_records[search_id][3] = email

                print("DATA UPDATED")
            else:
                print("====================================")
                print("\n\nNO RECORD FOUND")
                print("====================================")
            break
        continue

    elif choice == 'f':
        os.system('cls')
        print("Export Student Record")
                # file name , read / write
        with open('student_record.json', 'w') as new_file:
            json.dump(student_records, new_file, indent=4)

        print("DATA EXPORTED TO JSON")

        continue

    elif choice == 'g':
        os.system('cls')
        print("Import Student Record")
                # file name , read / write
        with open('student_record.json', 'r') as new_file:
            student_json = json.load(new_file)
        
        student_records = student_json
        print("DATA IMPORTED TO JSON")

        continue

    elif choice == 'h':
        print("System Exit")
        break

    else:
        print("\nINVALID CHOICE, please RE-ENTER YOUR CHOICE")
        continue