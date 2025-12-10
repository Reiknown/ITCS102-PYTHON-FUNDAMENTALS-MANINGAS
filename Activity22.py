import random

print("Let's guess the number")

random_number = random.randint(1, 10)
tries = 0
tuloy = True

while tuloy == True:
    num = int(eval(input("Input an integer number --> ")))
    tries += 1 

    if num == random_number: 
        print("CORRECT")
        print(f"The number is {num}")
        print(f"It only took you {tries} tries!")
        break
    else:
        print("WRONG \nContinue...")
        continue
