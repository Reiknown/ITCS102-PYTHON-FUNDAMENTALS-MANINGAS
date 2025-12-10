# Washing Machine Logic

isDirty = True #booleanm variable to initialize the loop

while isDirty == True:
    confirm = input("Do you wish to continue washing (yes / no) --> ").lower()

    if confirm == 'yes':
        print("continuing the cycle")
        continue
    elif confirm == 'no':
        print('cycle stops')
    else:
        print("invalid choice")
        continue
