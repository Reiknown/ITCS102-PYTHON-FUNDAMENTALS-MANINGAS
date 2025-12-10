# ANIME LIST

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
    print(f"- {anime}")
