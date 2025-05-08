alive = []
dead = []

with open('output.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()  
    if " - " in line:  
        name, status = line.split(" - ")
        if status == "alive":
            alive.append(name)
        elif status == "dead":
            dead.append(name)
    else:
        print(f"Skipping invalid line: {line}")  


with open('alivecharacters.txt', 'w') as alive_file:
    for character in alive:
        alive_file.write(f"{character}\n")

with open('deadcharacters.txt', 'w') as dead_file:
    for character in dead:
        dead_file.write(f"{character}\n")

print("Characters have been filtered.")