import random

with open('characters.txt', 'r') as file:
    characters = list(set(file.read().splitlines()))

status = ["alive", "dead"]

characters = [name.strip() for name in characters]

with open('output.txt', 'w') as file:
    for character in characters:
        character_status = random.choice(status)
        file.write(f"{character} - {character_status}\n")

print("Saved status of characters.")

  