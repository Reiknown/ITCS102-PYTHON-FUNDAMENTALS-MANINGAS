print("ODD NUMBER SUMMATION")
odd_sum = 0
for n in range(10):
    number = eval(input("Please enter an odd number: "))

    if number % 2 != 0:
        odd_sum += number
print("The sum of all odd numbers is", odd_sum)
