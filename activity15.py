odd_sum = 0

for i in range(1, 11):
    number = eval(input(f"{i} - Please enter a number: "))

    if number % 2 != 0:
        odd_sum += number

print("The sum of all odd numnber is", odd_sum)