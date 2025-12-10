import os
import json

os.system('cls')
print("STUDENT INFORMATION SYSTEM ")
print("=================================\n")


# empty dictionary
student_records = {}

while True:
    print("=================================")
    print("SELECT FROM THE OPTIONS BELOW ↓↓! \n A- Add Information \n B- Print All Record \n C- Search Student Record \n D- Delete a Student Record \n E- Edit / Modify Student Record \n F- Export Student Recrod \n G- Import Student Record \n\n X - Exit")
    choice = input("Your choice            ->   ").lower()
    

    if choice == 'a':
        os.system('cls')
        print("ADDING STUDENT INFORMATION")
        print("--------------------------\n")
        student_id = input("Key search for this student? | Use this pattern(course-IDNO) : ")

        # Check if ID exists before asking for names
        if student_id in student_records:
            print(f"\nERROR: Student ID {student_id} already exists!")
            input("Press Enter to return to menu...")
        else:
            first_name = input("Input student first name --> ").upper()
            last_name = input("Input student last name --> ").upper()
            course = input("Input student course --> ").upper()
            email = input("Input student email address --> ")
            os.system('cls')

            # adding record to our dictionary
            student_records[student_id] = [first_name, last_name, course, email]
            print("DATA SAVED....\n")
        continue


# search
    elif choice == 'b':
        os.system('cls')
        print("PRINTING STUDENT RECORD....")

        for id, record in student_records.items():
            print(f"Student ID ---> {id} <--- In student record: {record}\n")
        continue


    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD ")
        print("---------------------\n")

        search_id = input("Input ID to search: ")

        if search_id in student_records.keys():
            os.system('cls')
            print("============")
            print("RECORD FOUND")
            print("============")
            # print the record of search stduent
            for i in student_records[search_id]:
                print(f"-- {i}")
        else:
            print("===================")
            print("\n\nNO RECORD FOUND")
            print("===================")
        print()
        continue


    elif choice == 'd':
        os.system('cls')
        print("DELETE EXISTING RECORD")
        print("----------------------\n")

        search_id = input("Input ID to search: ")
        if search_id in student_records.keys():
                print("============")
                print("RECORD FOUND")
                print("============")
                # print the record of search stduent
                for i in student_records[search_id]:
                    print(f"-- {i}")

                student_records.pop(search_id)
                print("RECORD DELETED")
        else:
                print("===============")
                print("NO RECORD FOUND")
                print("===============")
        print()
        continue


    elif choice == 'e':
        os.system('cls')
        print(" STUDENT RECORD ")
        print("===========================")

        search_id = input("Input ID to search ---> ")

        if search_id in student_records.keys():
            print("===========================")
            print("\n\nRECORD FOUND")
            print("====================================")
            # print the record of search stduent
            for i in student_records[search_id]:
                print(f"-- {i}")

            print("\nENTER NEW DETAILS BELOW:")
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
            print("===========================")
            print("\n\nNO RECORD FOUND")
            print("====================================")
        
        input("\nPress Enter To Continue...")
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
        print("WARNING: This will crash if no file exists!")

        # Ask the user
        confirm = input("Do you have a saved 'student_record.json' file? (y/n): ").lower()
        
        if confirm == 'y':
            with open('student_record.json', 'r') as new_file:
                student_json = json.load(new_file)
        
            student_records = student_json
            print("DATA IMPORTED TO JSON")
        else:
            print("Import cancelled. Please 'Export' data first.")
        continue


    elif choice == 'x':
        print("System Exit")
        break

    else:
        os.system('cls')
        print("\nINVALID CHOICE, PLEASE RE-ENTER YOUR CHOICE")
        continue