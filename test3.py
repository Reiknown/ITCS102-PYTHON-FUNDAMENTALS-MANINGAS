import os
import random
import json
import time
from getpass import getpass 

os.system('cls')

# ==============================================================================
# SYSTEM FUNCTIONS
# ==============================================================================

def clearscreen():
    os.system('cls') 

def header(title):
    clearscreen()
    print("=" * 60)
    print(f"\t {title}")
    print("=" * 60)
    print("\n")

def show_requirements():
    clearscreen()
    print("=" * 60)
    print("\t\t PROGRAM REQUIREMENTS")
    print("=" * 60)
    print("\nTo ensure all features of this program work correctly,")
    print("please make sure the following are installed:\n")
    print("  [1] Python 3.x")
    print("  [2] 'pygame' Library (Required for Activity 28)")
    print("      -> Command: pip3 install pygame")
    print("\nNOTE: Activity 28 will crash if pygame is not installed.")
    print("=" * 60)
    input("\nPress ENTER to continue...")
    clearscreen()

# ==============================================================================
# ACTIVITIES (1-28)
# ==============================================================================

def activity1():
    clearscreen()
    print("DESCRIPTION: Printing Hello World")
    print("-" * 30)
    print("Hello World")

def activity2():
    clearscreen()
    print("\nDESCRIPTION: Input and Output")
    print("-" * 30)
    name = input("What is your name....? ")
    print("Hi" , name , "Welcome to the Matrix")

def activity3():
    clearscreen()
    print("DESCRIPTION: Escape Sequences (\\n, \\t)")
    print("-" * 30)
    print("Happy:)\t\tMonday")
    print("\n\tBSIT1A \n from \n\tDLL")
    print("The \n\tQuick \n\t\tBrown \n\t\t\tFox \n\t\t\t\tJumps \n\t\t\t\t\tOver \n\t\t\t\t\t\tThe \n\t\t\t\t\t\t\tLazy \n\t\t\t\t\t\t\t\tDog")

def activity4():
    clearscreen()
    print("DESCRIPTION: String Length Function")
    print("-" * 30)
    name = input("Type your whole name ---> ")
    print("Your name has" ,len(name), "characters")

def activity5():
    clearscreen()
    print("DESCRIPTION: Data Types & Eval")
    print("-" * 30)
    something = eval(input("Input something (numbers only) --> "))
    print("The data type of something is",type(something))
    answer = 6 + something
    print("the answer is", answer)

def activity6():
    clearscreen()
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
    clearscreen()
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
    clearscreen()
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
    clearscreen()
    print("DESCRIPTION: Logical Operators")
    print("-" * 30)
    username = 'hanniel'
    password = 'pogisisir123'
    print(not((username == 'haniel') or (password == 'pogiako123')))

def activity10():
    clearscreen()
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
    clearscreen()
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
    clearscreen()
    print("DESCRIPTION: For Loop (Range)")
    print("-" * 30)
    for i in range(1, 10, 2):
        print(i, 'hello world')

def activity13():
    clearscreen()
    print("DESCRIPTION: For Loop Summation")
    print("-" * 30)
    num = 0
    for i in range(1, 3):
        number = eval(input('Enter a number: '))
        num += number
        print('Pautang muna sa lunes babayaran sa halagang:', 'Php',num)
    print(num)

def activity14():
    clearscreen()
    print("DESCRIPTION: Descending For Loop")
    print("-" * 30)
    for x in range(20, 0, -1):
        print(x)

def activity15():
    clearscreen()
    print("DESCRIPTION: For Loop with Input")
    print("-" * 30)
    odd_sum = 0
    for i in range(1, 11):
        number = eval(input(f"{i} - Please enter a number: "))
        if number % 2 != 0:
            odd_sum += number
    print("The sum of all odd numnber is", odd_sum)

def activity16():
    clearscreen()
    print("DESCRIPTION: Horizontal Output")
    print("-" * 30)
    for i in range(1, 20):
        print(i, end="\t")
    print()

def activity17():
    clearscreen()
    print("DESCRIPTION: Nested Loop (Grid)")
    print("-" * 30)
    for c in range(1, 11, 1):
        for i in range(1, 11, 1):
                print(i, end=" ")
        print()

def activity18():
    clearscreen()
    print("DESCRIPTION: Nested Loop (Number Triangle)")
    print("-" * 30)
    for i in range(1, 11, 1):
        for c in range(1, i, 1):
            print(c, end=" ")
        print()

def activity19():
    clearscreen()
    print("DESCRIPTION: Nested Loop (Star Triangle)")
    print("-" * 30)
    for i in range(1, 11, 1):
        for c in range(1, i, 1):
            print("*", end=" ")
        print()

def activity20():
    clearscreen()
    print("DESCRIPTION: Nested Loop (Inverted Triangle)")
    print("-" * 30)
    for i in range(1, 11, 1):
        for d in range(10, i, -1):
            print("*", end = " ")
        print()

def activity21():
    clearscreen()
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
    clearscreen()
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
    clearscreen()
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
    clearscreen()
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
    from Activity24 import greater, summation
    print("\n")
    greater("HANNIEL")
    greater("REI")
    greater("MANINGAS")
    summation(11)
    summation(12)

def activity25():
    clearscreen()
    print("DESCRIPTION: Activity Compiler (Concepts)")
    print("-" * 30)
    print("Activity 25 was the prototype of this final project menu system!")

def activity26():
    clearscreen()
    print("DESCRIPTION: Dictionaries")
    print("-" * 30)
    prog = {'easy':'py','easy2':'css'}
    print(prog['easy2'])

def activity27():
    clearscreen()
    print("DESCRIPTION: Dictionary Functions")
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
    clearscreen()
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
        
        pygame.quit()
        
    game_loop()

# ==============================================================================
# CODE CHALLENGES (1-16)
# ==============================================================================

def code_challenge1():
    clearscreen()
    print("DESCRIPTION: Diamond Pattern Name")
    print("-" * 30)
    name = input("State your first & last name, please...")
    print("\n\n \t\t\t\t\t♦ \n\n\n \t\t\t\t♦\t\t♦ \n\n\n \t\t\t♦\t\t\t\t♦ \n\n\n \t\t♦\t\t\tHI\t\t\t♦ \n\n\n \t♦\t\t\t" , name , "\t\t\t♦ \n\n\n \t\t♦\t\t\t\t\t\t♦ \n\n\n \t\t\t♦\t\t\t\t♦ \n\n\n \t\t\t\t♦\t\t♦ \n\n\n \t\t\t\t\t♦")

def code_challenge2():
    clearscreen()
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
    clearscreen()
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
    clearscreen()
    print("DESCRIPTION: Even or Odd Checker")
    print("-" * 30)
    number = int(input("Input a number: "))
    if number % 2 == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")

def code_challenge5():
    clearscreen()
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
    clearscreen()
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
    clearscreen()
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
    clearscreen()
    print("DESCRIPTION: Multiplication Table")
    print("-" * 30)
    print("MULTIPLICATION TABLE MAKER")
    number = int(input("Enter a number: "))
    print("\nMultiplication table for", number,":")
    for i in range(1, 11):
        result = number * i
        print(number, "x", i, "=",result)

def code_challenge9():
    clearscreen()
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
    clearscreen()
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
    clearscreen()
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
    clearscreen()
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
    clearscreen()
    print("DESCRIPTION: Tree Pattern")
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
    clearscreen()
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
    clearscreen()
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
    clearscreen()
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
            clearscreen()
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
                            clearscreen()
                            activity1()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('print("Hello World")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Demonstrates the basic use of the print() function to display text.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '2': 
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
                            clearscreen()
                            activity2()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('name = input("What is your name....? ")\nprint("Hi" , name , "Welcome to the Matrix")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Demonstrates how to get user input() and concatenate it with a string.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '3': 
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
                            clearscreen()
                            activity3()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('print("Happy:)\\t\\tMonday")\nprint("\\n\\tBSIT1A \\n from \\n\\tDLL")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Uses escape sequences like \\n (newline) and \\t (tab) for formatting.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '4': 
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
                            clearscreen()
                            activity4()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('name = input("Type your whole name ---> ")\nprint("Your name has" ,len(name), "characters")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Uses the len() function to count the number of characters in a string.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '5': 
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
                            clearscreen()
                            activity5()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('something = eval(input("Input something (numbers only) --> "))\nprint("The data type of something is",type(something))')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Demonstrates type() checking and the use of eval() for flexible number input.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '0': 
                    break
                
        elif choice == 'B':
            clearscreen()
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
                            clearscreen()
                            activity6()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('n1 = eval(input("Enter the first number: "))\nn2 = eval(input("Enter the second number : "))\ns = n1 + n2\nprint("The sum of",n1, "and",n2, "is", s)')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Performs all basic arithmetic operations: (+, -, *, /, **, %, //).")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '7': 
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
                            clearscreen()
                            activity7()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('a = 5\na += 5\na = a + 5\nprint("the value of a is", a)')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Shows how assignment operators (+=, -=, etc.) modify a variable's value.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '8': 
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
                            clearscreen()
                            activity8()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('balance = 500\nwithdrawal = 1500\nprint(balance < withdrawal)')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Uses comparison operators (==, !=, >, <) to return Boolean values.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '9': 
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
                            clearscreen()
                            activity9()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print("username = 'hanniel'\npassword = 'pogisisir123'\nprint(not((username == 'haniel') or (password == 'pogiako123')))")
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Demonstrates logical operators (and, or, not) to combine conditions.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '10': 
                    while True:
                        print("=======================")
                        print("     ACTIVITY 10")
                        print("=======================")
                        print("\n[1] Run Program")
                        print("[2] View Source Code")
                        print("[3] View Explanation")
                        print("\n[0] Back")
                        sel = input("Select: ")
                        if sel == '1':
                            clearscreen()
                            activity10()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('if isPWD.lower() == "yes":\n    discount = fare * .2\n    new_fare = fare - discount')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("A conditional program (If-Else) that calculates fare based on PWD status.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '0': 
                    break

        elif choice == 'C':
            clearscreen()
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
                            clearscreen()
                            activity11()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('if temp >= 1 and temp <= 20:\n    print("Temperature outside is cold")\nelif temp >= 21 and temp <= 30:\n    print("Temperature outside is lukewarm")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Uses Elif statements to categorize temperature ranges (Cold, Warm, Hot).")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '12': 
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
                            clearscreen()
                            activity12()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print("for i in range(1, 10, 2):\n    print(i, 'hello world')")
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("A simple For Loop using range(start, stop, step) to print numbers.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '13': 
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
                            clearscreen()
                            activity13()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print("num = 0\nfor i in range(1, 3):\n    number = eval(input('Enter a number: '))\n    num += number")
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Calculates the sum of numbers entered by the user inside a loop.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '14': 
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
                            clearscreen()
                            activity14()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print("for x in range(20, 0, -1):\n    print(x)")
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Demonstrates a reverse for loop counting down from 20 to 0.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '15': 
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
                            clearscreen()
                            activity15()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('for i in range(1, 11):\n    number = eval(input(f"{i} - Please enter a number: "))\n    if number % 2 != 0:\n        odd_sum += number')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Loops through 10 inputs and sums only the odd numbers.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '0': 
                    break

        elif choice == 'D':
            clearscreen()
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
                            clearscreen()
                            activity16()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('for i in range(1, 20):\n    print(i, end="\\t")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Prints numbers horizontally using the 'end' parameter in print().")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '17': 
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
                            clearscreen()
                            activity17()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('for c in range(1, 11, 1):\n    for i in range(1, 11, 1):\n        print(i, end=" ")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Uses nested loops to create a square grid of numbers.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '18': 
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
                            clearscreen()
                            activity18()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('for i in range(1, 11, 1):\n    for c in range(1, i, 1):\n        print(c, end=" ")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Uses nested loops to create a triangle pattern made of numbers.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '19': 
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
                            clearscreen()
                            activity19()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('for i in range(1, 11, 1):\n    for c in range(1, i, 1):\n        print("*", end=" ")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Uses nested loops to create a standard triangle pattern using asterisks (*).")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '20': 
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
                            clearscreen()
                            activity20()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('for i in range(1, 11, 1):\n    for d in range(10, i, -1):\n        print("*", end = " ")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Uses nested loops to create an inverted triangle pattern.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '0': 
                    break

        elif choice == 'E':
            clearscreen()
            while True:
                print("================================")
                print("       ACTIVITIES 21-25")
                print("================================")
                print("\n[21] Act 21: Washing Machine")
                print("[22] Act 22: Guess Number")
                print("[23] Act 23: Lists")
                print("[24] Act 24: Functions")
                print("[24_1] Act 24_1: Import Sim")
                print("[25] Act 25: Compiler Concept")
                print("\n[0] Back")
                ch = input("Select: ")
                if ch == '21': 
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
                            clearscreen()
                            activity21()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('while isDirty == True:\n    confirm = input("Do you wish to continue washing (yes / no) --> ").lower()')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("A While Loop that continues running until the user says 'no'.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '22': 
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
                            clearscreen()
                            activity22()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('random_number = random.randint(1, 10)\nwhile tuloy == True:\n    num = int(eval(input("Input an integer number --> ")))')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("A guessing game using random.randint and a loop until correct.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '23': 
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
                            clearscreen()
                            activity23()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print("nm = ['apple','hotdog','orange','watermelon','egg']\nnm.append('mango')\nnm.pop()")
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Demonstrates list methods: append, pop, insert, and slicing.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '24': 
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
                            clearscreen()
                            activity24()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print("def greater(name):\n    print(f'Hi {name}, how are u ? ')\ngreater('HANNIEL')")
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Introduction to defining and calling custom functions (def).")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '24_1': 
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
                            clearscreen()
                            activity24_1()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print("# Redefining functions to simulate 'from Activity24 import...'\ndef greater(name):\n    print(f'Hi {name}, how are u ? ')")
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Simulates importing functions from a module.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '25': 
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
                            clearscreen()
                            activity25()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('print("Activity 25 was the prototype of this final project menu system!")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Conceptual activity showing the prototype of this menu system.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '0': 
                    break

        elif choice == 'F':
            clearscreen()
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
                            clearscreen()
                            activity26()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print("prog = {'easy':'py','easy2':'css'}\nprint(prog['easy2'])")
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Introduction to Dictionaries (Key-Value pairs) and accessing data.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '27': 
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
                            clearscreen()
                            activity27()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('empty_dictionary[keys] = value\nchoice = input("Would you like to continue adding anime...")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("A mini-database app using a Dictionary to Add, Search, and Print anime.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '28': 
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
                            clearscreen()
                            activity28()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('import pygame\npygame.init()\n# ... (Full Snake Game Code omitted for brevity) ...')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("A complete Snake Game using the 'pygame' external library.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '0': 
                    break

        elif choice == '0':
            break
        clearscreen()

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
                            clearscreen()
                            code_challenge1()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('print("\\t\\t\\t\\t\\t♦ \\n... " , name , " ...")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Prints a diamond pattern with the user's name in the center.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '2': 
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
                            clearscreen()
                            code_challenge2()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('libohan = halaga // 1000\nhalaga = halaga % 1000')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Breaks down a monetary amount into Philippine peso denominations.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '3': 
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
                            clearscreen()
                            code_challenge3()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('from getpass import getpass\nyourpassword = getpass("Type your password please --> ")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("A login system using the 'getpass' module to hide password input.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '4': 
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
                            clearscreen()
                            code_challenge4()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('if number % 2 == 0:\n    print(number, "is an even number")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Uses the modulo operator (%) to determine if a number is Even or Odd.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '5': 
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
                            clearscreen()
                            code_challenge5()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('if genre_choice == "action":\n    if length_choice == "short":\n        if decade_choice == "2000s" ...')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("A nested conditional program that recommends manga based on genre/length.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '0': 
                    break

        elif choice == 'B':
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
                            clearscreen()
                            code_challenge6()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('for i in range(number, 0, -1):\n    result *= i')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Calculates the factorial of a number using a loop and accumulation.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '7': 
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
                            clearscreen()
                            code_challenge7()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('if number % 2 != 0:\n    odd_sum += number')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Asks for 10 numbers and calculates the sum of the odd ones.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '8': 
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
                            clearscreen()
                            code_challenge8()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('for i in range(1, 11):\n    result = number * i')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Generates a multiplication table for a given number using a loop.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '9': 
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
                            clearscreen()
                            code_challenge9()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('for i in range(number, 0, -1):\n    print(i)\n    time.sleep(1)')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("A countdown timer that uses time.sleep(1) to pause execution.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '10': 
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
                            clearscreen()
                            code_challenge10()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print("for i in range(1, 11, 1):\n    for x in range(1, i, 1):\n        print('*', end=' ')")
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Creates the top half of a diamond pattern using nested loops.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '0': 
                    break

        elif choice == 'C':
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
                            clearscreen()
                            code_challenge11()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('for i in range(1, 13, 1):\n    for d in range(1, i, 1):\n        print("*", end=" ")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Prints a complex Hourglass pattern using multiple nested loops.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '12': 
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
                            clearscreen()
                            code_challenge12()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('for i in range(1, 7, 1):\n    for y in range(i, 0, -1):\n        print(y, end=" ")')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Prints an Arrow shape using loops for spacing and numbers.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '13': 
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
                            clearscreen()
                            code_challenge13()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('# DIAMOND\nfor i in range(1, 4):\n# TRIANGLES\nfor e in range(3):')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Prints a Christmas Tree shape (Triangles + Trunk).")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '14': 
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
                            clearscreen()
                            code_challenge14()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print('while number == True:\n    if num % 2 == 1:\n        odd += str(num) + ","\n        sum += num')
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Continually accepts numbers until '0' is pressed, then sums odd numbers.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '15': 
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
                            clearscreen()
                            code_challenge15()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print("while True:\n    if title.lower() == 'done':\n        break\n    anime_list.append(title)")
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("Uses a loop to add anime titles to a list until 'done' is typed.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '16': 
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
                            clearscreen()
                            code_challenge16()
                            input("Enter to continue...")
                        elif sel == '2':
                            clearscreen()
                            print("student_records = {}\nif choice == 'a':\n    student_records[student_id] = [first_name, last_name, course, email]")
                            input("Enter to continue...")
                        elif sel == '3':
                            clearscreen()
                            print("A full CRUD (Create, Read, Update, Delete) Student System using Dictionaries and JSON.")
                            input("Enter to continue...")
                        elif sel == '0':
                            break
                elif ch == '0': 
                    break

        elif choice == '0':
            break

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
            clearscreen()
            menu_activities()
        elif choice == '2':
            clearscreen()
            menu_challenges()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid Choice!")
            input("\nPress Enter to continue...")

main_menu()