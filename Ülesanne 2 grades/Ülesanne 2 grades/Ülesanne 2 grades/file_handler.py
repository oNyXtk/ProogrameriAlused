def read_grades():
    try:
        with open('grades.txt', 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_grades(nimi, hinned):
    with open('grades.txt', 'a') as file:
        hinned_str = ""
        for i in range(len(hinned)):
            hinned_str += str(hinned[i])  
            if i < len(hinned) - 1: 
                hinned_str += ", "
        
        file.write(f"Nimi: {nimi}\nHinded: {hinned_str}\n---\n")
