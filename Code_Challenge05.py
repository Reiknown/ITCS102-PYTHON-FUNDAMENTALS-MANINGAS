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
