import os
import random
import json
import time
# The getpass module is used in Code Challenge 3.
from getpass import getpass 

# ==============================================================================
# SYSTEM FUNCTIONS
# ==============================================================================

def clear_screen():
    os.system('cls') 

def header(title):
    clear_screen()
    print("=" * 60)
    # Using tabs \t to center manually
    print(f"\t\t\t {title}")
    print("=" * 60)
    print("\n")

def show_requirements():
    """Displays the list of requirements before the main menu starts."""
    clear_screen()
    print("=" * 60)
    print("\t\t PROGRAM REQUIREMENTS")
    print("=" * 60)
    print("\nTo ensure all features of this program work correctly,")
    print("please make sure the following are installed:\n")
    print("  [1] Python 3.x")
    print("  [2] 'pygame' Library (Required for Activity 28)")
    print("      -> Command: pip install pygame")
    print("\nNOTE: Activity 28 will crash if pygame is not installed.")
    print("=" * 60)
    input("\nPress Enter to continue...")

# ==============================================================================
# ACTIVITIES (1-28)
# ==============================================================================

def activity1():
    print("DESCRIPTION: Printing Hello World")
    print("-" * 30)
    print("Hello World")

def activity2():
    print("DESCRIPTION: Input and Output")
    print("-" * 30)
    name = input("What is your name....? ")
    print("Hi" , name , "Welcome to the Matrix")

def activity3():
    print("DESCRIPTION: Escape Sequences (\\n, \\t)")
    print("-" * 30)
    print("Happy:)\t\tMonday")
    print("\n\tBSIT1A \n from \n\tDLL")
    print("The \n\tQuick \n\t\tBrown \n\t\t\tFox \n\t\t\t\tJumps \n\t\t\t\t\tOver \n\t\t\t\t\t\tThe \n\t\t\t\t\t\t\tLazy \n\t\t\t\t\t\t\t\tDog")

def activity4():
    print("DESCRIPTION: String Length Function")
    print("-" * 30)
    name = input("Type your whole name ---> ")
    print("Your name has" ,len(name), "characters")

def activity5():
    print("DESCRIPTION: Data Types & Eval")
    print("-" * 30)
    something = eval(input("Input something (numbers only) --> "))
    print("The data type of something is",type(something))
    answer = 6 + something
    print("the answer is", answer)

def activity6():
    print("DESCRIPTION: Arithmetic Operators")
    print("-" * 30)
    n1 = eval(input("Enter the first number: "))
    n2 = eval(input("Enter the second number : "))
    s = n1 + n2
    d = n1 - n2
    p = n1 * n2
    q = n1 / n2
    
    # 'solution' variable removed as requested
    
    print("\nThe sum of",n1, "and",n2, "is", s)
    print("The difference of", n1, "and",n2,"is", d)
    print("The product of", n1, "and", n2, "is",p)
    print("The quotient of", n1, "and", n2, "is", q)
    print(n1, "exponent by", n2,"is", n1**n2)
    print("The remainder of", n1, "and",n2,"is", n1 % n2)
    print("The floor division of", n1, "and", n2, "is", n1//n2)

def activity7():
    print("DESCRIPTION: Assignment Operators")
    print("-" * 30)
    a = 5
    # print("the value of a is", a)
    a += 5
    # print("the value of a is", a)
    a = a + 5
    a += 3
    a += 8
    a += 2
    a -= 3
    a //= 5
    print("the value of a is", a)

def activity8():
    print("DESCRIPTION: Comparison Operators")
    print("-" * 30)
    balance = 500
    withdrawal = 1500
    b = 3
    a = 3
    name1 = 'hanniel'
    name2 = 'Hanniel'
    # print(balance < withdrawal)
    # print(b >= a)
    # print(name1 == name2)
    print(name1 != name2)

def activity9():
    print("DESCRIPTION: Logical Operators")
    print("-" * 30)
    username = 'hanniel'
    password = 'pogisisir123'
    # print(username == 'haniel')
    # print((username == 'haniel') and (password == 'pogisisir123'))
    # print((username == 'haniel') or (password == 'pogisisir123'))
    print(not((username == 'haniel') or (password == 'pogiako123')))

def activity10():
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
    print("DESCRIPTION: For Loop (Range)")
    print("-" * 30)
    for i in range(1, 10, 2):
        print(i, 'hello world')

def activity13():
    print("DESCRIPTION: For Loop Summation")
    print("-" * 30)
    num = 0
    for i in range(1, 11):
        number = eval(input('Enter a number: '))
        num += number
        print('paminta sibuyas bawang betsin isang boteng gin sa lunes babayaran sa halagang:', num)
    print(num)

def activity14():
    print("DESCRIPTION: Descending For Loop")
    print("-" * 30)
    for x in range(20, 0, -1):
        print(x)

def activity15():
    print("DESCRIPTION: For Loop with Input")
    print("-" * 30)
    odd_sum = 0
    for i in range(1, 11):
        number = eval(input(f"{i} - Please enter a number: "))
        if number % 2 != 0:
            odd_sum += number
    print("The sum of all odd numnber is", odd_sum)

def activity16():
    print("DESCRIPTION: Horizontal Output")
    print("-" * 30)
    for i in range(1, 20):
        print(i, end="\t")
    print()

def activity17():
    print("DESCRIPTION: Nested Loop (Grid)")
    print("-" * 30)
    for c in range(1, 11, 1):
        for i in range(1, 11, 1):
                print(i, end=" ")
        print()

def activity18():
    print("DESCRIPTION: Nested Loop (Number Triangle)")
    print("-" * 30)
    for i in range(1, 11, 1):
        for c in range(1, i, 1):
            print(c, end=" ")
        print()

def activity19():
    print("DESCRIPTION: Nested Loop (Star Triangle)")
    print("-" * 30)
    for i in range(1, 11, 1):
        for c in range(1, i, 1):
            print("*", end=" ")
        print()

def activity20():
    print("DESCRIPTION: Nested Loop (Inverted Triangle)")
    print("-" * 30)
    for i in range(1, 11, 1):
        for d in range(10, i, -1):
            print("*", end = " ")
        print()

def activity21():
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
    print("DESCRIPTION: While Loop (Guessing Game)")
    print("-" * 30)
    # import random is at the top of the file
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
    print("DESCRIPTION: Functions (Import Simulation)")
    print("-" * 30)
    
    # Redefining functions to simulate 'from Activity24 import...'
    def greater(name):
        print(f"Hi {name}, how are u ? ")

    def summation(x):
        sum = 0
        for y in range(x, 0, -1):
            sum += y
        print(f"The sum of {x} is {sum}")

    print("\n")
    greater("HANNIEL")
    greater("REI")
    greater("MANINGAS")
    summation(11)
    summation(12)

def activity25():
    print("DESCRIPTION: Activity Compiler (Concepts)")
    print("-" * 30)
    print("Activity 25 was the prototype of this final project menu system!")
    # NOTE: Running Act 25 inside here would be redundant (a menu inside a menu).

def activity26():
    print("DESCRIPTION: Dictionaries")
    print("-" * 30)
    prog = {'easy':'py','easy2':'css'}

    print(prog['easy2'])

def activity27():
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

        # adding data to a dictionary
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
    print("DESCRIPTION: Snake Game (Pygame)")
    print("-" * 30)
    
    # MODIFICATION: Import Pygame directly inside function
    import pygame
    
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
        # NOTE: Removed 'quit()' so the menu doesn't close
        
    game_loop()

# ==============================================================================
# CODE CHALLENGES (1-16)
# ==============================================================================

def code_challenge1():
    print("DESCRIPTION: Diamond Pattern Name")
    print("-" * 30)
    name = input("State your first & last name, please...")
    print("\n\n \t\t\t\t\t♦ \n\n\n \t\t\t\t♦\t\t♦ \n\n\n \t\t\t♦\t\t\t\t♦ \n\n\n \t\t♦\t\t\tHI\t\t\t♦ \n\n\n \t♦\t\t\t" , name , "\t\t\t♦ \n\n\n \t\t♦\t\t\t\t\t\t♦ \n\n\n \t\t\t♦\t\t\t\t♦ \n\n\n \t\t\t\t♦\t\t♦ \n\n\n \t\t\t\t\t♦")

def code_challenge2():
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
    print("DESCRIPTION: Even or Odd Checker")
    print("-" * 30)
    number = int(input("Input a number: "))
    if number % 2 == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")

def code_challenge5():
    print("DESCRIPTION: Manga Recommender")
    print("-" * 30)
    # --- Layer 1: Get user input for Genre ---
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
        print("Invalid genre selection. Please restart and choose action, romance, or horror.")

def code_challenge6():
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
    print("DESCRIPTION: Multiplication Table")
    print("-" * 30)
    print("MULTIPLICATION TABLE MAKER")
    number = int(input("Enter a number: "))
    print("\nMultiplication table for", number,":")
    for i in range(1, 11):
        result = number * i
        print(number, "x", i, "=",result)

def code_challenge9():
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
        header("ACTIVITIES MENU")
        print("[A] Activities 1 - 5")
        print("[B] Activities 6 - 10")
        print("[C] Activities 11 - 15")
        print("[D] Activities 16 - 20")
        print("[E] Activities 21 - 25")
        print("[F] Activities 26 - 28")
        print("[0] Back to Main Menu")
        
        choice = input("\nEnter Choice: ").upper()
        
        if choice == 'A':
            while True:
                header("ACTIVITIES 1-5")
                print("[1] Act 1: Hello World")
                print("[2] Act 2: Name Input")
                print("[3] Act 3: Formatting")
                print("[4] Act 4: String Length")
                print("[5] Act 5: Data Types")
                print("[0] Back")
                ch = input("Select: ")
                if ch == '1': 
                    activity1()
                    input("\nPress Enter to continue...")
                elif ch == '2': 
                    activity2()
                    input("\nPress Enter to continue...")
                elif ch == '3': 
                    activity3()
                    input("\nPress Enter to continue...")
                elif ch == '4': 
                    activity4()
                    input("\nPress Enter to continue...")
                elif ch == '5': 
                    activity5()
                    input("\nPress Enter to continue...")
                elif ch == '0': 
                    break
                
        elif choice == 'B':
            while True:
                header("ACTIVITIES 6-10")
                print("[6] Act 6: Arithmetic")
                print("[7] Act 7: Assignment")
                print("[8] Act 8: Comparison")
                print("[9] Act 9: Logic")
                print("[10] Act 10: Jeepney Fare")
                print("[0] Back")
                ch = input("Select: ")
                if ch == '6': 
                    activity6()
                    input("\nPress Enter to continue...")
                elif ch == '7': 
                    activity7()
                    input("\nPress Enter to continue...")
                elif ch == '8': 
                    activity8()
                    input("\nPress Enter to continue...")
                elif ch == '9': 
                    activity9()
                    input("\nPress Enter to continue...")
                elif ch == '10': 
                    activity10()
                    input("\nPress Enter to continue...")
                elif ch == '0': 
                    break

        elif choice == 'C':
            while True:
                header("ACTIVITIES 11-15")
                print("[11] Act 11: Temperature")
                print("[12] Act 12: Loop Hello")
                print("[13] Act 13: Loop Sum")
                print("[14] Act 14: Loop Descending")
                print("[15] Act 15: Odd Sum")
                print("[0] Back")
                ch = input("Select: ")
                if ch == '11': 
                    activity11()
                    input("\nPress Enter to continue...")
                elif ch == '12': 
                    activity12()
                    input("\nPress Enter to continue...")
                elif ch == '13': 
                    activity13()
                    input("\nPress Enter to continue...")
                elif ch == '14': 
                    activity14()
                    input("\nPress Enter to continue...")
                elif ch == '15': 
                    activity15()
                    input("\nPress Enter to continue...")
                elif ch == '0': 
                    break

        elif choice == 'D':
            while True:
                header("ACTIVITIES 16-20")
                print("[16] Act 16: Horizontal Print")
                print("[17] Act 17: Grid")
                print("[18] Act 18: Number Triangle")
                print("[19] Act 19: Star Triangle")
                print("[20] Act 20: Inverted Triangle")
                print("[0] Back")
                ch = input("Select: ")
                if ch == '16': 
                    activity16()
                    input("\nPress Enter to continue...")
                elif ch == '17': 
                    activity17()
                    input("\nPress Enter to continue...")
                elif ch == '18': 
                    activity18()
                    input("\nPress Enter to continue...")
                elif ch == '19': 
                    activity19()
                    input("\nPress Enter to continue...")
                elif ch == '20': 
                    activity20()
                    input("\nPress Enter to continue...")
                elif ch == '0': 
                    break

        elif choice == 'E':
            while True:
                header("ACTIVITIES 21-25")
                print("[21] Act 21: Washing Machine")
                print("[22] Act 22: Guess Number")
                print("[23] Act 23: Lists")
                print("[24] Act 24: Functions")
                print("[24.1] Act 24: Import Sim")
                print("[25] Act 25: Compiler Concept")
                print("[0] Back")
                ch = input("Select: ")
                if ch == '21': 
                    activity21()
                    input("\nPress Enter to continue...")
                elif ch == '22': 
                    activity22()
                    input("\nPress Enter to continue...")
                elif ch == '23': 
                    activity23()
                    input("\nPress Enter to continue...")
                elif ch == '24': 
                    activity24()
                    input("\nPress Enter to continue...")
                elif ch == '24.1': 
                    activity24_1()
                    input("\nPress Enter to continue...")
                elif ch == '25': 
                    activity25()
                    input("\nPress Enter to continue...")
                elif ch == '0': 
                    break

        elif choice == 'F':
            while True:
                header("ACTIVITIES 26-28")
                print("[26] Act 26: Dictionary")
                print("[27] Act 27: Dict Functions")
                print("[28] Act 28: Snake Game")
                print("[0] Back")
                ch = input("Select: ")
                if ch == '26': 
                    activity26()
                    input("\nPress Enter to continue...")
                elif ch == '27': 
                    activity27()
                    input("\nPress Enter to continue...")
                elif ch == '28': 
                    activity28()
                    input("\nPress Enter to continue...")
                elif ch == '0': 
                    break

        elif choice == '0':
            break

def menu_challenges():
    while True:
        header("CODE CHALLENGES MENU")
        print("[A] Challenges 1 - 5")
        print("[B] Challenges 6 - 10")
        print("[C] Challenges 11 - 16")
        print("[0] Back to Main Menu")
        
        choice = input("\nEnter Choice: ").upper()
        
        if choice == 'A':
            while True:
                header("CHALLENGES 1-5")
                print("[1] CC 1: Diamond Name")
                print("[2] CC 2: Money Denomination")
                print("[3] CC 3: Password")
                print("[4] CC 4: Even/Odd")
                print("[5] CC 5: Manga Recommender")
                print("[0] Back")
                ch = input("Select: ")
                if ch == '1': 
                    code_challenge1()
                    input("\nPress Enter to continue...")
                elif ch == '2': 
                    code_challenge2()
                    input("\nPress Enter to continue...")
                elif ch == '3': 
                    code_challenge3()
                    input("\nPress Enter to continue...")
                elif ch == '4': 
                    code_challenge4()
                    input("\nPress Enter to continue...")
                elif ch == '5': 
                    code_challenge5()
                    input("\nPress Enter to continue...")
                elif ch == '0': 
                    break

        elif choice == 'B':
            while True:
                header("CHALLENGES 6-10")
                print("[6] CC 6: Factorial")
                print("[7] CC 7: Odd Sum")
                print("[8] CC 8: Multiplication Table")
                print("[9] CC 9: Countdown")
                print("[10] CC 10: Diamond Top")
                print("[0] Back")
                ch = input("Select: ")
                if ch == '6': 
                    code_challenge6()
                    input("\nPress Enter to continue...")
                elif ch == '7': 
                    code_challenge7()
                    input("\nPress Enter to continue...")
                elif ch == '8': 
                    code_challenge8()
                    input("\nPress Enter to continue...")
                elif ch == '9': 
                    code_challenge9()
                    input("\nPress Enter to continue...")
                elif ch == '10': 
                    code_challenge10()
                    input("\nPress Enter to continue...")
                elif ch == '0': 
                    break

        elif choice == 'C':
            while True:
                header("CHALLENGES 11-16")
                print("[11] CC 11: Hourglass")
                print("[12] CC 12: Arrow")
                print("[13] CC 13: Tree")
                print("[14] CC 14: Odd Accumulator")
                print("[15] CC 15: Anime List")
                print("[16] CC 16: Student System")
                print("[0] Back")
                ch = input("Select: ")
                if ch == '11': 
                    code_challenge11()
                    input("\nPress Enter to continue...")
                elif ch == '12': 
                    code_challenge12()
                    input("\nPress Enter to continue...")
                elif ch == '13': 
                    code_challenge13()
                    input("\nPress Enter to continue...")
                elif ch == '14': 
                    code_challenge14()
                    input("\nPress Enter to continue...")
                elif ch == '15': 
                    code_challenge15()
                    input("\nPress Enter to continue...")
                elif ch == '16': 
                    code_challenge16()
                    input("\nPress Enter to continue...")
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
            menu_activities()
        elif choice == '2':
            menu_challenges()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid Choice!")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()