import os
import random
import json
import time
from getpass import getpass 

os.system('cls')

# ==============================================================================
# SYSTEM FUNCTIONS
# ==============================================================================

def header(title):
    os.system('cls')
    print("=" * 60)
    print(f"\t {title}")
    print("=" * 60)
    print("\n")

def show_requirements():
    os.system('cls')
    print("=" * 70)
    print("\t\t PROGRAM REQUIREMENTS & SETUP")
    print("=" * 70)
    print("\nTo ensure this program runs perfectly, please check the following:\n")

    print("  [1] SYSTEM CHECK: Python Version")
    print("      -> Recommended: Python 3.10 or newer")
    
    print("\n  [2] SETUP: Virtual Environment (Recommended)")
    print("   EX: Run these commands in your terminal to keep files organized:")
    print("      -> Create Env   : python -m venv name")
    print("      -> Activate Env : name\\Scripts\\activate") 
    
    print("\n  [3] REQUIRED LIBRARY: Pygame")
    print("      (This is required for Activity 28: Snake Game)")
    print("      -> Install      : pip install pygame")

    print("\n  NOTE: If 'pip' is not recognized, try using 'pip3'.")
    print("=" * 70)
    input("\nPress ENTER to start the program...")
    os.system('cls')

# ==============================================================================
# ACTIVITIES (1-28)
# ==============================================================================

def activity1():
    os.system('cls')
    print("DESCRIPTION: Printing Hello World")
    print("-" * 30)
    print("Hello World")

def activity2():
    os.system('cls')
    print("\nDESCRIPTION: Input and Output")
    print("-" * 30)
    name = input("What is your name....? ")
    print("Hi" , name , "Welcome to the Matrix")

def activity3():
    os.system('cls')
    print("DESCRIPTION: Escape Sequences (\\n, \\t)")
    print("-" * 30)
    print("Happy:)\t\tMonday")
    print("\n\tBSIT1A \n from \n\tDLL")
    print("The \n\tQuick \n\t\tBrown \n\t\t\tFox \n\t\t\t\tJumps \n\t\t\t\t\tOver \n\t\t\t\t\t\tThe \n\t\t\t\t\t\t\tLazy \n\t\t\t\t\t\t\t\tDog")

def activity4():
    os.system('cls')
    print("DESCRIPTION: String Length Function")
    print("-" * 30)
    name = input("Type your whole name ---> ")
    print("Your name has" ,len(name), "characters")

def activity5():
    os.system('cls')
    print("DESCRIPTION: Data Types & Eval")
    print("-" * 30)
    something = eval(input("Input something (numbers only) --> "))
    print("The data type of something is",type(something))
    answer = 6 + something
    print("the answer is", answer)

def activity6():
    os.system('cls')
    print("DESCRIPTION: Arithmetic Operators")
    print("-" * 30)
    n1 = eval(input("Enter the first number: "))
    n2 = eval(input("Enter the second number : "))
    s = n1 + n2
    d = n1 - n2
    p = n1 * n2
    q = n1 / n2
    print("\nThe sum of",n1, "and",n2, "is", s)
    print("The difference of", n1, "and",n2,"is", d)
    print("The product of", n1, "and", n2, "is",p)
    print("The quotient of", n1, "and", n2, "is", q)
    print(n1, "exponent by", n2,"is", n1**n2)
    print("The remainder of", n1, "and",n2,"is", n1 % n2)
    print("The floor division of", n1, "and", n2, "is", n1//n2)

def activity7():
    os.system('cls')
    print("DESCRIPTION: Assignment Operators")
    print("-" * 30)
    a = 5
    a += 5
    a = a + 5
    a += 3
    a += 8
    a += 2
    a -= 3
    a //= 5
    print("the value of a is", a)

def activity8():
    os.system('cls')
    print("DESCRIPTION: Comparison Operators")
    print("-" * 30)
    balance = 500
    withdrawal = 1500
    b = 3
    a = 3
    name1 = 'hanniel'
    name2 = 'Hanniel'
    print(name1 != name2)

def activity9():
    os.system('cls')
    print("DESCRIPTION: Logical Operators")
    print("-" * 30)
    username = 'hanniel'
    password = 'pogisisir123'
    print(not((username == 'haniel') or (password == 'pogiako123')))

def activity10():
    os.system('cls')
    print("DESCRIPTION: Conditional Statements (Jeepney Fare)")
    print("-" * 30)
    name = input("What is your name: ")
    isPWD = input("Are you a PWD (Yes / No) --> ")
    fare = eval(input("bayad --> ₱ "))

    if isPWD.lower() == "yes":
        discount = fare * .2
        new_fare = fare - discount
        print("Hi", name, ",", "PWD discount is ₱",discount, " Discounted fare is ₱",new_fare)
    else:
        print("Sorry!´•︵•`", name, "you are NOT eligible for PWD discount ,", "Amount to pay --> ₱", fare)

def activity11():
    os.system('cls')
    print("DESCRIPTION: Elif Statements (Temperature)")
    print("-" * 30)
    temp = eval(input("Enter temperature -->"))
    if temp >= 1 and temp <= 20:
        print("Temperature outside is cold")
    elif temp >= 21 and temp <= 30:
        print("Temperature outside is lukewarm")
    elif temp >= 31 and temp <= 40:
        print("Temperature outside is warm")
    elif temp >= 41 and temp <= 50:
        print("Temperature outside is hot")
    elif temp >= 51:
        print("Temperature outside is super hot")
    else:
        print("Invalid temperature")

def activity12():
    os.system('cls')
    print("DESCRIPTION: For Loop (Range)")
    print("-" * 30)
    for i in range(1, 10, 2):
        print(i, 'hello world')

def activity13():
    os.system('cls')
    print("DESCRIPTION: For Loop Summation")
    print("-" * 30)
    num = 0
    for i in range(1, 4):
        number = eval(input('Enter a number: '))
        num += number
        print('Pautang muna sa lunes babayaran sa halagang:', 'Php',num)
    print(num)

def activity14():
    os.system('cls')
    print("DESCRIPTION: Descending For Loop")
    print("-" * 30)
    for x in range(20, 0, -1):
        print(x)

def activity15():
    os.system('cls')
    print("DESCRIPTION: Loop with Input (Odd Sum)")
    print("-" * 30)
    odd_sum = 0
    for i in range(1, 11):
        number = eval(input(f"{i} - Please enter a number: "))
        if number % 2 != 0:
            odd_sum += number
    print("The sum of all odd numnber is", odd_sum)

def activity16():
    os.system('cls')
    print("DESCRIPTION: Horizontal Output")
    print("-" * 30)
    for i in range(1, 20):
        print(i, end="\t")
    print()

def activity17():
    os.system('cls')
    print("DESCRIPTION: Nested Loop (Grid)")
    print("-" * 30)
    for c in range(1, 11, 1):
        for i in range(1, 11, 1):
                print(i, end=" ")
        print()

def activity18():
    os.system('cls')
    print("DESCRIPTION: Nested Loop (Number Triangle)")
    print("-" * 30)
    for i in range(1, 11, 1):
        for c in range(1, i, 1):
            print(c, end=" ")
        print()

def activity19():
    os.system('cls')
    print("DESCRIPTION: Nested Loop (Star Triangle)")
    print("-" * 30)
    for i in range(1, 11, 1):
        for c in range(1, i, 1):
            print("*", end=" ")
        print()

def activity20():
    os.system('cls')
    print("DESCRIPTION: Nested Loop (Inverted Triangle)")
    print("-" * 30)
    for i in range(1, 11, 1):
        for d in range(10, i, -1):
            print("*", end = " ")
        print()

def activity21():
    os.system('cls')
    print("DESCRIPTION: While Loop (Washing Machine)")
    print("-" * 30)
    isDirty = True
    while isDirty == True:
        confirm = input("Do you wish to continue washing (yes / no) --> ").lower()
        if confirm == 'yes':
            print("continuing the cycle")
            continue
        elif confirm == 'no':
            print('cycle stops')
            break
        else:
            print("invalid choice")
            continue

def activity22():
    os.system('cls')
    print("DESCRIPTION: While Loop (Guessing Game)")
    print("-" * 30)
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

def activity23():
    os.system('cls')
    print("DESCRIPTION: Lists & Methods")
    print("-" * 30)
    nm = ['apple','hotdog','orange','watermelon','egg']
    nm.append('mango')
    print(nm)

    nm.pop()
    print(nm)

    nm.insert(0,'watermelon')
    print(nm)

    for i in nm:
        print(f"{i}  in the basket")

    mi = 'HANNIEL MANINGAS'
    for u in mi:
        print(u)
        
    print("\nReversed")
    for q in mi[::-1]:
        print(q)

def activity24():
    os.system('cls')
    print("DESCRIPTION: Functions (Def)")
    print("-" * 30)
    def greater(name):
        print(f"Hi {name}, how are u ? ")

    def summation(x):
        sum = 0
        for y in range(x, 0, -1):
            sum += y
        print(f"The sum of {x} is {sum}")

    greater('HANNIEL')
    greater('REI')
    greater('MANINGAS')
    summation(10)
    summation(9)
    summation(8)

def activity24_1():
    os.system('cls')
    print("DESCRIPTION: Modules & Imports")
    print("-" * 30)
    from Activity24 import greater, summation
    print("\n")
    greater("HANNIEL")
    greater("REI")
    greater("MANINGAS")
    summation(11)
    summation(12)

def activity25():
    os.system('cls')
    print("DESCRIPTION: Activity Compiler (Concepts)")
    print("-" * 30)
    print("Activity 25 was the prototype of this final project menu system!")

def activity26():
    os.system('cls')
    print("DESCRIPTION: Dictionaries")
    print("-" * 30)
    prog = {'easy':'py','easy2':'css'}
    print(prog['easy2'])

def activity27():
    os.system('cls')
    print("DESCRIPTION: Dictionary App (Anime DB)")
    print("-" * 30)
    print("Adding Data to dictionary")
    print(" =============================== ")
    tuloy = True
    empty_dictionary = {}

    def print_anime():
        for i,j in empty_dictionary.items():
            print(f"CODE {i} | TITLE -- {j}")

    def pang_search(key):
        print("Searching ..... ")
        print(f" result shows {empty_dictionary[key]} on our database") 

    while tuloy == True:
        keys = input("Input keys for this anime ---> ")
        value = input("Enter anime title ---> ")
        empty_dictionary[keys] = value
        choice = input("Would you like to continue adding anime \ny-YES\nn-NO\np-PRINT\ns-SEARCH--->  ").lower()

        if choice == 'y':
            print("Continuing.... ")
            continue
        elif choice == 'n':
            print("Program Stops")
            break
        elif choice == 'p':
            print_anime()
            continue
        elif choice == 's':
            code = input("Please input the code of the anime: ")
            pang_search(code)
        else:
            print("Invalid Choice!")
            continue

def activity28():
    os.system('cls')
    print("DESCRIPTION: Snake Game (Pygame)")
    print("-" * 30)
    
    import pygame
    
    pygame.init()
    width = 600
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    clock = pygame.time.Clock()
    speed = 10
    snake_block = 10
    font_style = pygame.font.SysFont(None, 30)

    def draw_snake(snake_list):
        for block in snake_list:
            pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

    def game_loop():
        game_over = False
        game_close = False
        x = width / 2
        y = height / 2
        x_change = 0
        y_change = 0
        snake_list = []
        length_of_snake = 1
        food_x = round(random.randrange(0, width - snake_block) / 10) * 10
        food_y = round(random.randrange(0, height - snake_block) / 10) * 10

        while not game_over:
            while game_close:
                screen.fill(black)
                message = font_style.render('You Lost! Press Q-Quit or C-Play Again', True, red)
                screen.blit(message, [width / 6, height / 3])
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        elif event.key == pygame.K_c:
                            game_loop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -snake_block
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = snake_block
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -snake_block
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = snake_block
                        x_change = 0
            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True
            x += x_change
            y += y_change
            screen.fill(black)
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
            snake_head = [x, y]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]
            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_close = True
            draw_snake(snake_list)
            pygame.display.update()
            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, width - snake_block) / 10) * 10
                food_y = round(random.randrange(0, height - snake_block) / 10) * 10
                length_of_snake += 1
            clock.tick(speed)
        
    game_loop()
    pygame.quit()

# ==============================================================================
# CODE CHALLENGES (1-16)
# ==============================================================================

def code_challenge1():
    os.system('cls')
    print("DESCRIPTION: Diamond Pattern Name")
    print("-" * 30)
    name = input("State your first & last name, please...")
    print("\n\n \t\t\t\t\t♦ \n\n\n \t\t\t\t♦\t\t♦ \n\n\n \t\t\t♦\t\t\t\t♦ \n\n\n \t\t♦\t\t\tHI\t\t\t♦ \n\n\n \t♦\t\t\t" , name , "\t\t\t♦ \n\n\n \t\t♦\t\t\t\t\t\t♦ \n\n\n \t\t\t♦\t\t\t\t♦ \n\n\n \t\t\t\t♦\t\t♦ \n\n\n \t\t\t\t\t♦")

def code_challenge2():
    os.system('cls')
    print("DESCRIPTION: Money Denomination")
    print("-" * 30)
    halaga = eval(input("\t\t\t\tIlagay ang halagang ide-deposito: "))
    print("\tNarito ang paghahati gamit ang denominasyon sa Pilipinas:")
    libohan = halaga // 1000 
    halaga = halaga % 1000
    print("\t\t\t\t\t\t\t\t", libohan, "- ₱1000")
    limandaanan = halaga // 500
    halaga = halaga % 500
    print("\n\t\t\t\t\t\t\t", limandaanan, "- ₱500")
    dalawandaanan = halaga // 200
    halaga = halaga % 200
    print("\n\t\t\t\t\t\t", dalawandaanan, "- ₱200")
    isandaanan = halaga // 100
    halaga = halaga % 100
    print("\n\t\t\t\t\t", isandaanan, "- ₱100")
    limampuan = halaga // 50
    halaga = halaga % 50
    print("\n\t\t\t\t", limampuan, "- ₱50")
    dalawampuan = halaga // 20
    halaga = halaga % 20
    print("\n\t\t\t", dalawampuan, "- ₱20")
    sampuan = halaga // 10
    halaga = halaga % 10
    print("\n\t\t", sampuan, "- ₱10")
    limahan = halaga // 5
    halaga = halaga % 5
    print("\n\t", limahan, "- ₱5")
    isahan = halaga // 1
    halaga = halaga % 1
    print("\n", isahan, "- ₱1")

def code_challenge3():
    os.system('cls')
    print("DESCRIPTION: Password Access")
    print("-" * 30)
    username = "Maningas"
    password = "Hanniel"
    yourusername = input("HI what is your username --> ")
    yourpassword = getpass("Type your password please --> ")
    if yourusername == username and yourpassword == password:
        print('Access Granted')
    else:
        print('Access Denied')

def code_challenge4():
    os.system('cls')
    print("DESCRIPTION: Even or Odd Checker")
    print("-" * 30)
    number = int(input("Input a number: "))
    if number % 2 == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")

def code_challenge5():
    os.system('cls')
    print("DESCRIPTION: Manga Recommender")
    print("-" * 30)
    print("Welcome to the Manga Reader Recommender!")
    print("Answer a few questions to find your next read.")
    genre_choice = input("What genre do you like? (action, romance, horror): ").lower()

    if genre_choice == "action":
        print("\nYou selected: Action")
        length_choice = input("How long should the manga be? (short, medium, long): ").lower()
        if length_choice == "short":
            print("You selected: Short")
            decade_choice = input("Which decade? (2000s / 2010s): ").lower()
            if decade_choice == "2000s" or decade_choice == "2000":
                print("\n--- Short Action Manga from the 2000s ---")
                print("1. Baccano!\n2. Black Lagoon\n3. Afro Samurai")
            elif decade_choice == "2010s" or decade_choice == "2010":
                print("\n--- Short Action Manga from the 2010s ---")
                print("1. Puella Magi Madoka Magica\n2. One-Punch Man Season 1\n3. Devilman Crybaby")
        elif length_choice == "medium":
            print("You selected: Medium")
            decade_choice = input("Which decade? (2000s / 2010s): ").lower()
            if decade_choice == "2000s" or decade_choice == "2000":
                print("\n--- Medium Action Manga from the 2000s ---")
                print("1. Fullmetal Alchemist: Brotherhood\n2. Code Geass\n3. Tengen Toppa Gurren Lagann")
            elif decade_choice == "2010s" or decade_choice == "2010":
                print("\n--- Medium Action Manga from the 2010s ---")
                print("1. Attack on Titan\n2. Psycho-Pass\n3. Demon Slayer")
        elif length_choice == "long":
            print("You selected: Long")
            decade_choice = input("Which decade? (2000s / 2010s): ").lower()
            if decade_choice == "2000s" or decade_choice == "2000":
                print("\n--- Long Action Manga from the 2000s ---")
                print("1. Naruto\n2. Bleach\n3. One Piece")
            elif decade_choice == "2010s" or decade_choice == "2010":
                print("\n--- Long Action Manga from the 2010s ---")
                print("1. Hunter x Hunter\n2. JoJo's Bizarre Adventure\n3. My Hero Academia")

    elif genre_choice == "romance":
        print("\nYou selected: Romance")
        length_choice = input("How long should the manga be? (short, medium, long): ").lower()
        if length_choice == "short":
            print("You selected: Short")
            decade_choice = input("Which decade? (2000s / 2010s): ").lower()
            if decade_choice == "2000s" or decade_choice == "2000":
                print("\n--- Short Romance Manga from the 2000s ---")
                print("1. The Girl Who Leapt Through Time\n2. 5 Centimeters Per Second\n3. Paradise Kiss")
            elif decade_choice == "2010s" or decade_choice == "2010":
                print("\n--- Short Romance Manga from the 2010s ---")
                print("1. Your Name\n2. A Silent Voice\n3. Rascal Does Not Dream of Bunny Girl Senpai")
        elif length_choice == "medium":
            print("You selected: Medium")
            decade_choice = input("Which decade? (2000s / 2010s): ").lower()
            if decade_choice == "2000s" or decade_choice == "2000":
                print("\n--- Medium Romance Manga from the 2000s ---")
                print("1. Toradora!\n2. Clannad + After Story\n3. Ouran High School Host Club")
            elif decade_choice == "2010s" or decade_choice == "2010":
                print("\n--- Medium Romance Manga from the 2010s ---")
                print("1. Your Lie in April\n2. Chihayafuru\n3. My Love Story!!")
        elif length_choice == "long":
            print("You selected: Long")
            decade_choice = input("Which decade? (2000s / 2010s): ").lower()
            if decade_choice == "2000s" or decade_choice == "2000":
                print("\n--- Long Romance Manga from the 2000s ---")
                print("1. Inuyasha\n2. Nana\n3. Skip Beat!")
            elif decade_choice == "2010s" or decade_choice == "2010":
                print("\n--- Long Romance Manga from the 2010s ---")
                print("1. Fruits Basket\n2. Nisekoi: False Love\n3. The World God Only Knows")

    elif genre_choice == "horror":
        print("\nYou selected: Horror")
        length_choice = input("How long should the manga be? (short, medium, long): ").lower()
        if length_choice == "short":
            print("You selected: Short")
            decade_choice = input("Which decade? (2000s / 2010s): ").lower()
            if decade_choice == "2000s" or decade_choice == "2000":
                print("\n--- Short Horror Manga from the 2000s ---")
                print("1. Perfect Blue\n2. Gyo: Tokyo Fish Attack\n3. Blood: The Last Vampire")
            elif decade_choice == "2010s" or decade_choice == "2010":
                print("\n--- Short Horror Manga from the 2010s ---")
                print("1. The Promised Neverland Season 1\n2. Made in Abyss\n3. Another")
        elif length_choice == "medium":
            print("You selected: Medium")
            decade_choice = input("Which decade? (2000s / 2010s): ").lower()
            if decade_choice == "2000s" or decade_choice == "2000":
                print("\n--- Medium Horror Manga from the 2000s ---")
                print("1. Monster\n2. Higurashi: When They Cry\n3. Hellsing Ultimate")
            elif decade_choice == "2010s" or decade_choice == "2010":
                print("\n--- Medium Horror Manga from the 2010s ---")
                print("1. Parasyte: The Maxim\n2. Shiki\n3. Tokyo Ghoul")
        elif length_choice == "long":
            print("You selected: Long")
            decade_choice = input("Which decade? (2000s / 2010s): ").lower()
            if decade_choice == "2000s" or decade_choice == "2000":
                print("\n--- Long Horror Manga from the 2000s ---")
                print("1. Gantz\n2. D.Gray-man\n3. Claymore")
            elif decade_choice == "2010s" or decade_choice == "2010":
                print("\n--- Long Horror Manga from the 2010s ---")
                print("1. Dorohedoro\n2. Berserk\n3. Ajin: Demi-Human")
    else:
        print("Invalid genre selection.")

def code_challenge6():
    os.system('cls')
    print("DESCRIPTION: Factorial Calculator")
    print("-" * 30)
    print("FACTORIAL PROGRAM")
    number = eval(input("Please enter a number: "))
    result = 1
    for i in range(number, 0, -1):
        previous_result = result
        result *= i
        print(previous_result, "*", i, "=", result)
    print("Factorial of",number,"is", result)

def code_challenge7():
    os.system('cls')
    print("DESCRIPTION: Odd Number Summation")
    print("-" * 30)
    print("ODD NUMBER SUMMATION")
    odd_sum = 0
    for n in range(10):
        number = eval(input("Please enter an odd number: "))
        if number % 2 != 0:
            odd_sum += number
    print("The sum of all odd numbers is", odd_sum)

def code_challenge8():
    os.system('cls')
    print("DESCRIPTION: Multiplication Table")
    print("-" * 30)
    print("MULTIPLICATION TABLE MAKER")
    number = int(input("Enter a number: "))
    print("\nMultiplication table for", number,":")
    for i in range(1, 11):
        result = number * i
        print(number, "x", i, "=",result)

def code_challenge9():
    os.system('cls')
    print("DESCRIPTION: Countdown Timer")
    print("-" * 30)
    print("⏳ COUNTDOWN TIMER SIMULATOR")
    number = int(input("Enter the starting number for countdown: "))
    print("\nCountdown started:")
    for i in range(number, 0, -1):
        print(i)
        time.sleep(1)
    print("Liftoff!")

def code_challenge10():
    os.system('cls')
    print("DESCRIPTION: Diamond Top Pattern")
    print("-" * 30)
    print("\t\t *", end=' ')
    for i in range(1, 11, 1):
        for y in range(10, i, -1):
            print(" ", end=' ')
        for x in range(1, i, 1):
            print("*", end=' ')
        for z in range(1, i, 1):
            print("*", end=' ')
        print()

def code_challenge11():
    os.system('cls')
    print("DESCRIPTION: Hourglass Pattern")
    print("-" * 30)
    for i in range(1, 13, 1):
        for c in range(12, i, -1):
            print(" ", end=" ")
        for d in range(1, i, 1):
                print("*", end=" ")
        for e in range(0, i, 1):
                print("*", end=" ")
        print()
    for i in range(1, 13, 1):
        for c in range(0, i, 1):
            print(" ", end=" ")
        for d in range(11, i, -1):
            print("*", end=" ")
        for e in range(12, i, -1):
            print("*", end=" ")
        print()

def code_challenge12():
    os.system('cls')
    print("DESCRIPTION: Arrow Pattern")
    print("-" * 30)
    for i in range(1, 7, 1):
        for x in range(7, i, -1):
            print(" ", end=' ')
        for y in range(i, 0, -1):
            print(y, end=" ")
        for z in range(2,i + 1,1):
            print(z, end=" ")
        print()

def code_challenge13():
    os.system('cls')
    print("DESCRIPTION: Christmas Tree Pattern")
    print("-" * 30)
    # DIAMOND
    for i in range(1, 4):
        for a in range(4 - i):
            print(" ", end=" ")
        for b in range(i + i - 1):
            print("*", end=" ")
        print()
    for i in range(2, 0, -1):
        for c in range(4 - i):
            print(" ", end=" ")
        for d in range(i + i - 1):
            print("*", end=" ")
        print()
    # TRIANGLES
    for e in range(3):
        for i in range(1, 5):
            for f in range(4 - i):
                print(" ", end=" ")
            for g in range(i + i - 1):
                print("*", end=" ")
            print()
    # TRUNK
    for g in range(3):
        for i in range(2):
            print(" ", end=" ")
        print("*", end=" ")
        print(" ", end=" ")
        print("*", end=" ")
        print()

def code_challenge14():
    os.system('cls')
    print("DESCRIPTION: Odd Number Accumulator")
    print("-" * 30)
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

def code_challenge15():
    os.system('cls')
    print("DESCRIPTION: Anime List Loop")
    print("-" * 30)
    anime_list = []
    print("--- Favorite Anime Collector ---")
    print("Enter your favorite anime titles...")
    print("Type 'done' when you are finished.\n")
    while True:
        title = input("Enter anime title: ")
        if title.lower() == 'done':
            print("\nCollection Completed.....")
            break
        else:
            anime_list.append(title)
            print(f"Added '{title}' to the list.")
    print("\nHere is the complete list of your favorite anime!! ~^,^~")
    for anime in anime_list:
        print(f"- {anime}")

def code_challenge16():
    os.system('cls')
    print("DESCRIPTION: Student Information System")
    print("-" * 30)
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

# ==============================================================================
# MENU FUNCTIONS
# ==============================================================================

def menu_activities():
    while True:
        print("================================")
        print("       ACTIVITIES MENU")
        print("================================")
        print("\n[A] Activities 1 - 5")
        print("\n[B] Activities 6 - 10")
        print("\n[C] Activities 11 - 15")
        print("\n[D] Activities 16 - 20")
        print("\n[E] Activities 21 - 25")
        print("\n[F] Activities 26 - 28")
        print("\n\n[0] Back to Main Menu")
        
        choice = input("\nEnter Choice: ").upper()
        
        if choice == 'A':
            os.system('cls')
            while True:
                print("================================")
                print("       ACTIVITIES 1-5")
                print("================================")
                print("\n[1] Act 1: Hello World")
                print("[2] Act 2: Name Input")
                print("[3] Act 3: Formatting")
                print("[4] Act 4: String Length")
                print("[5] Act 5: Data Types")
                print("\n[0] Back")
                ch = input("Select: ")
                if ch == '1': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("      ACTIVITY 1")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity1()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print('print("Hello World")')
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Demonstrates the basic use of the print() function to display text.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '2': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("      ACTIVITY 2")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity2()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """name = input("What is your name....? ")
print("Hi" , name , "Welcome to the Matrix")"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Demonstrates how to get user input() and concatenate it with a string.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '3': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("      ACTIVITY 3")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity3()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""print("Happy:)\t\tMonday")
print("\n\tBSIT1A \n from \n\tDLL")
print("The \n\tQuick \n\t\tBrown \n\t\t\tFox \n\t\t\t\tJumps \n\t\t\t\t\tOver \n\t\t\t\t\t\tThe \n\t\t\t\t\t\t\tLazy \n\t\t\t\t\t\t\t\tDog")""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Uses escape sequences like \\n (newline) and \\t (tab) for formatting.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '4': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("      ACTIVITY 4")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity4()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """name = input("Type your whole name ---> ")
print("Your name has" ,len(name), "characters")"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Uses the len() function to count the number of characters in a string.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '5': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("      ACTIVITY 5")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity5()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """something = eval(input("Input something (numbers only) --> "))
print("The data type of something is",type(something))
answer = 6 + something
print("the answer is", answer)"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Demonstrates type() checking and the use of eval() for flexible number input.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '0': 
                    break
                
        elif choice == 'B':
            os.system('cls')
            while True:
                print("================================")
                print("       ACTIVITIES 6-10")
                print("================================")
                print("\n[6] Act 6: Arithmetic")
                print("[7] Act 7: Assignment")
                print("[8] Act 8: Comparison")
                print("[9] Act 9: Logic")
                print("[10] Act 10: Jeepney Fare")
                print("\n[0] Back")
                ch = input("Select: ")
                if ch == '6': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("      ACTIVITY 6")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity6()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """n1 = eval(input("Enter the first number: "))
n2 = eval(input("Enter the second number : "))
s = n1 + n2
d = n1 - n2
p = n1 * n2
q = n1 / n2
print("\nThe sum of",n1, "and",n2, "is", s)
print("The difference of", n1, "and",n2,"is", d)
print("The product of", n1, "and", n2, "is",p)
print("The quotient of", n1, "and", n2, "is", q)
print(n1, "exponent by", n2,"is", n1**n2)
print("The remainder of", n1, "and",n2,"is", n1 % n2)
print("The floor division of", n1, "and", n2, "is", n1//n2)"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Performs all basic arithmetic operations: (+, -, *, /, **, %, //).")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '7': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("      ACTIVITY 7")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity7()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """a = 5
a += 5
a = a + 5
a += 3
a += 8
a += 2
a -= 3
a //= 5
print("the value of a is", a)"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Shows how assignment operators (+=, -=, etc.) modify a variable's value.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '8': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("      ACTIVITY 8")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity8()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """balance = 500
withdrawal = 1500
b = 3
a = 3
name1 = 'hanniel'
name2 = 'Hanniel'
print(name1 != name2)"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Uses comparison operators (==, !=, >, <) to return Boolean values.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '9': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("      ACTIVITY 9")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity9()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """username = 'hanniel'
password = 'pogisisir123'
print(not((username == 'haniel') or (password == 'pogiako123')))"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Demonstrates logical operators (and, or, not) to combine conditions.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '10': 
                    while True:
                        os.system('cls')
                        print("=======================")
                        print("     ACTIVITY 10")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity10()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """name = input("What is your name: ")
isPWD = input("Are you a PWD (Yes / No) --> ")
fare = eval(input("bayad --> ₱ "))

if isPWD.lower() == "yes":
    discount = fare * .2
    new_fare = fare - discount
    print("Hi", name, ",", "PWD discount is ₱",discount, " Discounted fare is ₱",new_fare)
else:
    print("Sorry!´•︵•`", name, "you are NOT eligible for PWD discount ,", "Amount to pay --> ₱", fare)"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("A conditional program (If-Else) that calculates fare based on PWD status.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '0': 
                    break

        elif choice == 'C':
            os.system('cls')
            while True:
                print("================================")
                print("       ACTIVITIES 11-15")
                print("================================")
                print("\n[11] Act 11: Temperature")
                print("[12] Act 12: Loop Hello")
                print("[13] Act 13: Loop Sum")
                print("[14] Act 14: Loop Descending")
                print("[15] Act 15: Odd Sum")
                print("\n[0] Back")
                ch = input("Select: ")
                if ch == '11': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 11")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity11()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """temp = eval(input("Enter temperature -->"))
if temp >= 1 and temp <= 20:
    print("Temperature outside is cold")
elif temp >= 21 and temp <= 30:
    print("Temperature outside is lukewarm")
elif temp >= 31 and temp <= 40:
    print("Temperature outside is warm")
elif temp >= 41 and temp <= 50:
    print("Temperature outside is hot")
elif temp >= 51:
    print("Temperature outside is super hot")
else:
    print("Invalid temperature")"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Uses Elif statements to categorize temperature ranges (Cold, Warm, Hot).")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '12': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 12")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity12()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """for i in range(1, 10, 2):
    print(i, 'hello world')"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("A simple For Loop using range(start, stop, step) to print numbers.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '13': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 13")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity13()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """num = 0
for i in range(1, 4):
    number = eval(input('Enter a number: '))
    num += number
    print('Pautang muna sa lunes babayaran sa halagang:', 'Php',num)
print(num)"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Calculates the sum of numbers entered by the user inside a loop.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '14': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 14")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity14()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """for x in range(20, 0, -1):
    print(x)"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Demonstrates a reverse for loop counting down from 20 to 1.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '15': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 15")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity15()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """odd_sum = 0
for i in range(1, 11):
    number = eval(input(f"{i} - Please enter a number: "))
    if number % 2 != 0:
        odd_sum += number
print("The sum of all odd numnber is", odd_sum)"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Loops through 10 inputs and sums only the odd numbers.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '0': 
                    break

        elif choice == 'D':
            os.system('cls')
            while True:
                print("================================")
                print("       ACTIVITIES 16-20")
                print("================================")
                print("\n[16] Act 16: Horizontal Print")
                print("[17] Act 17: Grid")
                print("[18] Act 18: Number Triangle")
                print("[19] Act 19: Star Triangle")
                print("[20] Act 20: Inverted Triangle")
                print("\n[0] Back")
                ch = input("Select: ")
                if ch == '16': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 16")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity16()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""for i in range(1, 20):
    print(i, end="\t")
print()""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Prints numbers horizontally using the 'end' parameter in print().")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '17': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 17")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity17()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """for c in range(1, 11, 1):
    for i in range(1, 11, 1):
        print(i, end=" ")
    print()"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Uses nested loops to create a square grid of numbers.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '18': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 18")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity18()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """for i in range(1, 11, 1):
    for c in range(1, i, 1):
        print(c, end=" ")
    print()"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Uses nested loops to create a triangle pattern made of numbers.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '19': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 19")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity19()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """for i in range(1, 11, 1):
    for c in range(1, i, 1):
        print("*", end=" ")
    print()"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Uses nested loops to create a standard triangle pattern using asterisks (*).")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '20': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 20")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity20()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """for i in range(1, 11, 1):
    for d in range(10, i, -1):
        print("*", end = " ")
    print()"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Uses nested loops to create an inverted triangle pattern.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '0': 
                    break

        elif choice == 'E':
            os.system('cls')
            while True:
                print("================================")
                print("       ACTIVITIES 21-25")
                print("================================")
                print("\n[21] Act 21: Washing Machine")
                print("[22] Act 22: Guess Number")
                print("[23] Act 23: Lists")
                print("[24] Act 24: Functions")
                print("[24_1] Act 24_1: Modules (Activity 24)")
                print("[25] Act 25: Compiler Concept")
                print("\n[0] Back")
                ch = input("Select: ")
                if ch == '21': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 21")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity21()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            code = """isDirty = True
while isDirty == True:
    confirm = input("Do you wish to continue washing (yes / no) --> ").lower()
    if confirm == 'yes':
        print("continuing the cycle")
        continue
    elif confirm == 'no':
        print('cycle stops')
        break
    else:
        print("invalid choice")
        continue"""
                            print(code)
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("A While Loop that continues running until the user says 'no'.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '22': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 22")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity22()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""print("Let's guess the number")
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
        continue""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("A guessing game using random.randint and a loop until correct.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '23': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 23")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity23()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""nm = ['apple','hotdog','orange','watermelon','egg']
nm.append('mango')
print(nm)

nm.pop()
print(nm)

nm.insert(0,'watermelon')
print(nm)

for i in nm:
    print(f"{i}  in the basket")

mi = 'HANNIEL MANINGAS'
for u in mi:
    print(u)
        
print("\nReversed")
for q in mi[::-1]:
    print(q)""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Demonstrates list methods: append, pop, insert, and slicing.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '24': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 24")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity24()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""def greater(name):
    print(f"Hi {name}, how are u ? ")

def summation(x):
    sum = 0
    for y in range(x, 0, -1):
        sum += y
    print(f"The sum of {x} is {sum}")

greater('HANNIEL')
greater('REI')
greater('MANINGAS')
summation(10)
summation(9)
summation(8)""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Introduction to defining and calling custom functions (def).")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '24_1': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 24_1")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity24_1()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""from Activity24 import greater, summation
print("\n")
greater("HANNIEL")
greater("REI")
greater("MANINGAS")
summation(11)
summation(12)""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Demonstrates code reusability by importing functions (greater, summation) from the external Activity24.py file.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '25': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 25")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity25()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""from Activity25_1 import *
from Activity25_2 import *

tuloy = True

while tuloy:
    print("\n\t*********************************************")
    print("\t     ACTIVITY/CODE CHALLENGE COMPILER      ")
    print("\t*********************************************")
    print("\t\t--- ACTIVITIES ---")
    print("\tA1 - Activity 1")
    print("\tA2 - Activity 2")
    print("\tA3 - Activity 3")
    print("\tA4 - Activity 4")
    print("\tA5 - Activity 5")
    print("\n\t\t--- CODE CHALLENGES ---")
    print("\tC1 - Code Challenge 1")
    print("\tC2 - Code Challenge 2")
    print("\tC3 - Code Challenge 3")
    print("\tC4 - Code Challenge 4")
    print("\n\t0  - Exit")
    print("\t*********************************************")

    ask = input("\tWhich file would you like to run? ").upper()

    if ask == 'A1':
        activity1()
    elif ask == 'A2':
        activity2()
    elif ask == 'A3':
        activity3()
    elif ask == 'A4':
        activity4()
    elif ask == 'A5':
        activity5()
    elif ask == 'C1':
        code_challenge1()
    elif ask == 'C2':
        code_challenge2()
    elif ask == 'C3':
        code_challenge3()
    elif ask == 'C4':
        code_challenge4()
    elif ask == '0':
        tuloy = False
        print("\n\tProgram Ended")
    else:
        print("\n\tInvalid Input! \nPlease choose from the list (ex: A1, C1)")""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Conceptual activity showing the prototype of this menu system.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '0': 
                    break

        elif choice == 'F':
            os.system('cls')
            while True:
                print("================================")
                print("       ACTIVITIES 26-28")
                print("================================")
                print("\n[26] Act 26: Dictionary")
                print("[27] Act 27: Dict Functions")
                print("[28] Act 28: Snake Game")
                print("\n[0] Back")
                ch = input("Select: ")
                if ch == '26': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 26")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity26()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""prog = {'easy':'py','easy2':'css'}
print(prog['easy2'])""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Introduction to Dictionaries (Key-Value pairs) and accessing data.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '27': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 27")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity27()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""print("Adding Data to dictionary")
print(" =============================== ")
tuloy = True
empty_dictionary = {}

def print_anime():
    for i,j in empty_dictionary.items():
        print(f"CODE {i} | TITLE -- {j}")

def pang_search(key):
    print("Searching ..... ")
    print(f" result shows {empty_dictionary[key]} on our database") 

while tuloy == True:
    keys = input("Input keys for this anime ---> ")
    value = input("Enter anime title ---> ")
    empty_dictionary[keys] = value
    choice = input("Would you like to continue adding anime \ny-YES\nn-NO\np-PRINT\ns-SEARCH--->  ").lower()

    if choice == 'y':
        print("Continuing.... ")
        continue
    elif choice == 'n':
        print("Program Stops")
        break
    elif choice == 'p':
        print_anime()
        continue
    elif choice == 's':
        code = input("Please input the code of the anime: ")
        pang_search(code)
    else:
        print("Invalid Choice!")
        continue""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("A mini-database app using a Dictionary to Add, Search, and Print anime.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '28': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("     ACTIVITY 28")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            activity28()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""# SNAKE GAME

#Step 1 
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Screen size
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors (RGB)
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Game speed and block size
clock = pygame.time.Clock()
speed = 10
snake_block = 10

# Font for messages
font_style = pygame.font.SysFont(None, 30)


#Step 2 
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

#Step 3 
def game_loop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    # Generate first food
    food_x = round(random.randrange(0, width - snake_block) / 10) * 10
    food_y = round(random.randrange(0, height - snake_block) / 10) * 10

    while not game_over:

        # Loss screen
        while game_close:
            screen.fill(black)
            message = font_style.render('You Lost! Press Q-Quit or C-Play Again', True, red)
            screen.blit(message, [width / 6, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        # Event handling (keyboard)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Check if snake hits the wall
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # Update position
        x += x_change
        y += y_change

        # Draw background and food
        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

        # Add snake head
        snake_head = [x, y]
        snake_list.append(snake_head)

        # Remove extra segments if not growing
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake
        draw_snake(snake_list)

        # Update display
        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10) * 10
            food_y = round(random.randrange(0, height - snake_block) / 10) * 10
            length_of_snake += 1

        # Control game speed
        clock.tick(speed)

    # Quit Pygame
    pygame.quit()

# Start the game
game_loop()""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("A complete Snake Game using the 'pygame' external library.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '0': 
                    break

        elif choice == '0':
            break
        os.system('cls')

def menu_challenges():
    while True:
        print("================================")
        print("     CODE CHALLENGES MENU")
        print("================================")
        print("\n[A] Challenges 1 - 5")
        print("\n[B] Challenges 6 - 10")
        print("\n[C] Challenges 11 - 16")
        print("\n\n[0] Back to Main Menu")
        
        choice = input("\nEnter Choice: ").upper()
        
        if choice == 'A':
            os.system('cls')
            while True:
                print("================================")
                print("        CHALLENGES 1-5")
                print("================================")
                print("\n[1] CC 1: Diamond Name")
                print("[2] CC 2: Money Denomination")
                print("[3] CC 3: Password")
                print("[4] CC 4: Even/Odd")
                print("[5] CC 5: Manga Recommender")
                print("\n[0] Back")
                ch = input("Select: ")
                if ch == '1': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 1")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge1()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""name = input("State your first & last name, please...")
    print("\n\n \t\t\t\t\t♦ \n\n\n \t\t\t\t♦\t\t♦ \n\n\n \t\t\t♦\t\t\t\t♦ \n\n\n \t\t♦\t\t\tHI\t\t\t♦ \n\n\n \t♦\t\t\t" , name , "\t\t\t♦ \n\n\n \t\t♦\t\t\t\t\t\t♦ \n\n\n \t\t\t♦\t\t\t\t♦ \n\n\n \t\t\t\t♦\t\t♦ \n\n\n \t\t\t\t\t♦")""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Prints a diamond pattern with the user's name in the center.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '2': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 2")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge2()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""halaga = eval(input("\t\t\t\tIlagay ang halagang ide-deposito: "))
print("\tNarito ang paghahati gamit ang denominasyon sa Pilipinas:")
libohan = halaga // 1000 
halaga = halaga % 1000
print("\t\t\t\t\t\t\t\t", libohan, "- ₱1000")
limandaanan = halaga // 500
halaga = halaga % 500
print("\n\t\t\t\t\t\t\t", limandaanan, "- ₱500")
dalawandaanan = halaga // 200
halaga = halaga % 200
print("\n\t\t\t\t\t\t", dalawandaanan, "- ₱200")
isandaanan = halaga // 100
halaga = halaga % 100
print("\n\t\t\t\t\t", isandaanan, "- ₱100")
limampuan = halaga // 50
halaga = halaga % 50
print("\n\t\t\t\t", limampuan, "- ₱50")
dalawampuan = halaga // 20
halaga = halaga % 20
print("\n\t\t\t", dalawampuan, "- ₱20")
sampuan = halaga // 10
halaga = halaga % 10
print("\n\t\t", sampuan, "- ₱10")
limahan = halaga // 5
halaga = halaga % 5
print("\n\t", limahan, "- ₱5")
isahan = halaga // 1
halaga = halaga % 1
print("\n", isahan, "- ₱1")""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Breaks down a monetary amount into Philippine peso denominations.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '3': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 3")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge3()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""username = "Maningas"
password = "Hanniel"
yourusername = input("HI what is your username --> ")
yourpassword = getpass("Type your password please --> ")
if yourusername == username and yourpassword == password:
    print('Access Granted')
else:
    print('Access Denied')""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("A login system using the 'getpass' module to hide password input.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '4': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 4")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge4()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""number = int(input("Input a number: "))
if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Uses the modulo operator (%) to determine if a number is Even or Odd.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '5': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 5")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge5()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""# --- Layer 1: Get user input for Genre ---
print("Welcome to the Manga Reader Recommender!")
print("Answer a few questions to find your next read.")
genre_choice = input("What genre do you like? (action, romance, horror): ").lower()

# --- ACTION BRANCH ---
if genre_choice == "action":
    print("\nYou selected: Action")

    # --- Layer 2: Get user input for Length ---
    length_choice = input("How long should the manga be? (short, medium, long): ").lower()

    # --- Action | Short ---
    if length_choice == "short":
        print("You selected: Short")

        # --- Layer 3: Get user input for Decade ---
        decade_choice = input("Which decade? (2000s / 2010s): ").lower()

        if decade_choice == "2000s" or decade_choice == "2000":
            print("\n--- Short Action Manga from the 2000s ---")
            print("1. Baccano!")
            print("2. Black Lagoon")
            print("3. Afro Samurai")
        elif decade_choice == "2010s" or decade_choice == "2010":
            print("\n--- Short Action Manga from the 2010s ---")
            print("1. Puella Magi Madoka Magica")
            print("2. One-Punch Man Season 1")
            print("3. Devilman Crybaby")
        else:
            print("Invalid decade selected.")

    # --- Action | Medium ---
    elif length_choice == "medium":
        print("You selected: Medium")
        decade_choice = input("Which decade? (2000s / 2010s): ").lower()

        if decade_choice == "2000s" or decade_choice == "2000":
            print("\n--- Medium Action Manga from the 2000s ---")
            print("1. Fullmetal Alchemist: Brotherhood")
            print("2. Code Geass: Lelouch of the Rebellion")
            print("3. Tengen Toppa Gurren Lagann")
        elif decade_choice == "2010s" or decade_choice == "2010":
            print("\n--- Medium Action Manga from the 2010s ---")
            print("1. Attack on Titan")
            print("2. Psycho-Pass")
            print("3. Demon Slayer: Kimetsu no Yaiba")
        else:
            print("Invalid decade selected.")

    # --- Action | Long ---
    elif length_choice == "long":
        print("You selected: Long")
        decade_choice = input("Which decade? (2000s / 2010s): ").lower()

        if decade_choice == "2000s" or decade_choice == "2000":
            print("\n--- Long Action Manga from the 2000s ---")
            print("1. Naruto")
            print("2. Bleach")
            print("3. One Piece")
        elif decade_choice == "2010s" or decade_choice == "2010":
            print("\n--- Long Action Manga from the 2010s ---")
            print("1. Hunter x Hunter")
            print("2. JoJo's Bizarre Adventure")
            print("3. My Hero Academia")
        else:
            print("Invalid decade selected.")
    else:
        print("Invalid length selected.")

# --- ROMANCE BRANCH ---
elif genre_choice == "romance":
    print("\nYou selected: Romance")
    length_choice = input("How long should the manga be? (short, medium, long): ").lower()

    # --- Romance | Short ---
    if length_choice == "short":
        print("You selected: Short")
        decade_choice = input("Which decade? (2000s / 2010s): ").lower()

        if decade_choice == "2000s" or decade_choice == "2000":
            print("\n--- Short Romance Manga from the 2000s ---")
            print("1. The Girl Who Leapt Through Time")
            print("2. 5 Centimeters Per Second")
            print("3. Paradise Kiss")
        elif decade_choice == "2010s" or decade_choice == "2010":
            print("\n--- Short Romance Manga from the 2010s ---")
            print("1. Your Name")
            print("2. A Silent Voice")
            print("3. Rascal Does Not Dream of Bunny Girl Senpai")
        else:
            print("Invalid decade selected.")

    # --- Romance | Medium ---
    elif length_choice == "medium":
        print("You selected: Medium")
        decade_choice = input("Which decade? (2000s / 2010s): ").lower()

        if decade_choice == "2000s" or decade_choice == "2000":
            print("\n--- Medium Romance Manga from the 2000s ---")
            print("1. Toradora!")
            print("2. Clannad + After Story")
            print("3. Ouran High School Host Club")
        elif decade_choice == "2010s" or decade_choice == "2010":
            print("\n--- Medium Romance Manga from the 2010s ---")
            print("1. Your Lie in April")
            print("2. Chihayafuru")
            print("3. My Love Story!!")
        else:
            print("Invalid decade selected.")

    # --- Romance | Long ---
    elif length_choice == "long":
        print("You selected: Long")
        decade_choice = input("Which decade? (2000s / 2010s): ").lower()

        if decade_choice == "2000s" or decade_choice == "2000":
            print("\n--- Long Romance Manga from the 2000s ---")
            print("1. Inuyasha")
            print("2. Nana")
            print("3. Skip Beat!")
        elif decade_choice == "2010s" or decade_choice == "2010":
            print("\n--- Long Romance Manga from the 2010s ---")
            print("1. Fruits Basket")
            print("2. Nisekoi: False Love")
            print("3. The World God Only Knows")
        else:
            print("Invalid decade selected.")
    else:
        print("Invalid length selected.")

# --- HORROR BRANCH ---
elif genre_choice == "horror":
    print("\nYou selected: Horror")
    length_choice = input("How long should the manga be? (short, medium, long): ").lower()

    # --- Horror | Short ---
    if length_choice == "short":
        print("You selected: Short")
        decade_choice = input("Which decade? (2000s / 2010s): ").lower()

        if decade_choice == "2000s" or decade_choice == "2000":
            print("\n--- Short Horror Manga from the 2000s ---")
            print("1. Perfect Blue")
            print("2. Gyo: Tokyo Fish Attack")
            print("3. Blood: The Last Vampire")
        elif decade_choice == "2010s" or decade_choice == "2010":
            print("\n--- Short Horror Manga from the 2010s ---")
            print("1. The Promised Neverland Season 1")
            print("2. Made in Abyss")
            print("3. Another")
        else:
            print("Invalid decade selected.")

    # --- Horror | Medium ---
    elif length_choice == "medium":
        print("You selected: Medium")
        decade_choice = input("Which decade? (2000s / 2010s): ").lower()

        if decade_choice == "2000s" or decade_choice == "2000":
            print("\n--- Medium Horror Manga from the 2000s ---")
            print("1. Monster")
            print("2. Higurashi: When They Cry")
            print("3. Hellsing Ultimate")
        elif decade_choice == "2010s" or decade_choice == "2010":
            print("\n--- Medium Horror Manga from the 2010s ---")
            print("1. Parasyte: The Maxim")
            print("2. Shiki")
            print("3. Tokyo Ghoul")
        else:
            print("Invalid decade selected.")

    # --- Horror | Long ---
    elif length_choice == "long":
        print("You selected: Long")
        decade_choice = input("Which decade? (2000s / 2010s): ").lower()

        if decade_choice == "2000s" or decade_choice == "2000":
            print("\n--- Long Horror Manga from the 2000s ---")
            print("1. Gantz")
            print("2. D.Gray-man")
            print("3. Claymore")
        elif decade_choice == "2010s" or decade_choice == "2010":
            print("\n--- Long Horror Manga from the 2010s ---")
            print("1. Dorohedoro")
            print("2. Berserk")
            print("3. Ajin: Demi-Human")
        else:
            print("Invalid decade selected.")
    else:
        print("Invalid length selected.")

# --- For Invalid Genre ---
else:
    print("Invalid genre selection. Please restart and choose action, romance, or horror.")""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("A nested conditional program that recommends manga based on genre/length.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '0': 
                    break

        elif choice == 'B':
            os.system('cls')
            while True:
                print("================================")
                print("        CHALLENGES 6-10")
                print("================================")
                print("\n[6] CC 6: Factorial")
                print("[7] CC 7: Odd Sum")
                print("[8] CC 8: Multiplication Table")
                print("[9] CC 9: Countdown")
                print("[10] CC 10: Diamond Top")
                print("\n[0] Back")
                ch = input("Select: ")
                if ch == '6': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 6")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge6()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""print("FACTORIAL PROGRAM")
number = eval(input("Please enter a number: "))
result = 1
for i in range(number, 0, -1):
    previous_result = result
    result *= i
    print(previous_result, "*", i, "=", result)
print("Factorial of",number,"is", result)""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Calculates the factorial of a number using a loop and accumulation.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '7': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 7")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge7()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""print("DESCRIPTION: Odd Number Summation")
    print("-" * 30)
    print("ODD NUMBER SUMMATION")
    odd_sum = 0
    for n in range(10):
        number = eval(input("Please enter an odd number: "))
        if number % 2 != 0:
            odd_sum += number
    print("The sum of all odd numbers is", odd_sum)""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Asks for 10 numbers and calculates the sum of the odd ones.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '8': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 8")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge8()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""print("DESCRIPTION: Multiplication Table")
print("-" * 30)
print("MULTIPLICATION TABLE MAKER")
number = int(input("Enter a number: "))
print("\nMultiplication table for", number,":")
for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=",result)""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Generates a multiplication table for a given number using a loop.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '9': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 9")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge9()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""print("⏳ COUNTDOWN TIMER SIMULATOR")
    number = int(input("Enter the starting number for countdown: "))
    print("\nCountdown started:")
    for i in range(number, 0, -1):
        print(i)
        time.sleep(1)
    print("Liftoff!")""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("A countdown timer that uses time.sleep(1) to pause execution.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '10': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 10")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge10()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""print("\t\t *", end=' ')
for i in range(1, 11, 1):
    for y in range(10, i, -1):
        print(" ", end=' ')
    for x in range(1, i, 1):
        print("*", end=' ')
    for z in range(1, i, 1):
        print("*", end=' ')
    print()""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Creates the top half of a diamond pattern using nested loops.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '0': 
                    break

        elif choice == 'C':
            os.system('cls')
            while True:
                print("================================")
                print("       CHALLENGES 11-16")
                print("================================")
                print("[11] CC 11: Hourglass")
                print("[12] CC 12: Arrow")
                print("[13] CC 13: Tree")
                print("[14] CC 14: Odd Accumulator")
                print("[15] CC 15: Anime List")
                print("[16] CC 16: Student System")
                print("[0] Back")
                ch = input("Select: ")
                if ch == '11': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 11")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge11()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""for i in range(1, 13, 1):
    for c in range(12, i, -1):
        print(" ", end=" ")
    for d in range(1, i, 1):
            print("*", end=" ")
    for e in range(0, i, 1):
            print("*", end=" ")
    print()
for i in range(1, 13, 1):
    for c in range(0, i, 1):
        print(" ", end=" ")
    for d in range(11, i, -1):
        print("*", end=" ")
    for e in range(12, i, -1):
        print("*", end=" ")
    print()""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Prints a complex Hourglass pattern using multiple nested loops.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '12': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 12")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge12()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""for i in range(1, 7, 1):
    for x in range(7, i, -1):
        print(" ", end=' ')
    for y in range(i, 0, -1):
        print(y, end=" ")
    for z in range(2,i + 1,1):
        print(z, end=" ")
    print()""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Prints an Arrow shape using loops for spacing and numbers.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '13': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 13")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge13()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""# DIAMOND
for i in range(1, 3 + 1):
    for a in range(4 - i):
        print(" ", end=" ")
    for b in range(i + i - 1):
        print("*", end=" ")
    print()
for i in range(2, 0, -1):
    for c in range(4 - i):
        print(" ", end=" ")
    for d in range(i + i - 1):
        print("*", end=" ")
    print()

# TRIANGLES
for e in range(3):
    for i in range(1, 4 + 1):
        for f in range(4 - i):
            print(" ", end=" ")
        for g in range(i + i - 1):
            print("*", end=" ")
        print()

# TRUNK
for g in range(3):
    for i in range(2):
        print(" ", end=" ")
    print("*", end=" ")
    print(" ", end=" ")
    print("*", end=" ")
    print()""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Prints a Christmas Tree shape (Triangles + Trunk).")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '14': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 14")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge14()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""name = input('Hi! What is your name? --> ')
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
print(f"All the ODD numbers you input is {odd}")""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Continually accepts numbers until '0' is pressed, then sums odd numbers.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '15': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 15")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge15()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""# ANIME LIST

# CREATE EMPTY LIST
anime_list = []

print("--- Favorite Anime Collector ---")
print("Enter your favorite anime titles...")
print("Type 'done' when you are finished.\n")

# INPUT
while True:
    title = input("Enter anime title: ")

    # ONCE DONE
    if title.lower() == 'done':
        print("\nCollection Completed.....")
        break
    else:
        anime_list.append(title)
        print(f"Added '{title}' to the list.")

# FINAL OUTPUT
print("\nHere is the complete list of your favorite anime!! ~^,^~")

# INTERATE
for anime in anime_list:
    print(f"- {anime}")""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("Uses a loop to add anime titles to a list until 'done' is typed.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '16': 
                    os.system('cls')
                    while True:
                        print("=======================")
                        print("   CODE CHALLENGE 16")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            os.system('cls')
                            code_challenge16()
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '2':
                            os.system('cls')
                            print(r"""import os
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
        continue""")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '3':
                            os.system('cls')
                            print("A full CRUD (Create, Read, Update, Delete) Student System using Dictionaries and JSON.")
                            input("\n\nEnter to continue...")
                            os.system('cls')
                        elif sel == '0':
                            os.system('cls')
                            break
                elif ch == '0': 
                    break

        elif choice == '0':
            break
        os.system('cls')

# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================

def main_menu():
    show_requirements()
    
    name = input("Please enter your name: ").upper()
    while True:
        header(f"WELCOME {name} TO MY FINALS PROJECT")
        print("Finals Project by: Hanniel Rei L. Maningas")
        print("Section: BSIT 1A")
        print("-" * 60)
        print("[1] ACTIVITIES")
        print("[2] CODE CHALLENGES")
        print("[0] EXIT PROGRAM")
        print("-" * 60)
        
        choice = input("Enter Choice: ")
        
        if choice == '1':
            os.system('cls')
            menu_activities()
        elif choice == '2':
            os.system('cls')
            menu_challenges()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid Choice!")
            input("\nPress Enter to continue...")
main_menu()