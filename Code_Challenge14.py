name = input('Hi! What is your name? --> ')
print("++++++++++++++++++++++++++++++++++")
print("ODD number compiler, type '0' to terminate the loop" )

sum = 0
odd = " "
number = True

while number == True:
    num = eval(input("Enter a number --> "))

    if num % 2 == 1:
        print("ODD number detected")
        odd += str(num) + ","
        sum += num
        continue

    elif num == 0:
        print("Loop Terminated")
        break

    else:
        if num % 2 == 0:
            print("EVEN number detected")
        else:
            print("Invalid number")
            continue

print(f"Hi {name} the sum of all ODD number is {sum}")
print(f"All the ODD numbers you input is {odd}")
