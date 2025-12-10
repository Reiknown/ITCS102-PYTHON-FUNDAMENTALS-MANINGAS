print("FACTORIAL PROGRAM")

number = eval(input("Please enter a number: "))

result = 1
for i in range(number, 0, -1):
    previous_result = result
    result *= i
    print(previous_result, "*", i, "=", result)

print("Factorial of",number,"is", result)
