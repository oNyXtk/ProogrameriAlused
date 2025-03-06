from file_handler import write_grades, read_grades

def add_student(nimi, hinned):
    write_grades(nimi, hinned)
    print("Õpilane lisatud!")

def view_students():
    students = read_grades()
    if students:
        print("\nKõik õpilased ja nende hinded:")
        for student in students:
            print(student.strip())  
    else:
        print("Õpilasi ei leitud.")

def search_student(nimi):
    students = read_grades()
    found = False
    for line in students:
        if nimi in line:
            found = True
            print("Õpilase andmed:", line.strip())
            break
    if not found:
        print(f"Õpilast nimega '{nimi}' ei leitud.")

def calculate_average(nimi):
    students = read_grades()
    for line in students:
        if line.startswith(f"Nimi: {nimi}"):
            hinned_line = next(students)
            hinned_str = hinned_line.strip().split(': ')[1]  
            hinned = []  
            
            
            for grade in hinned_str.split(', '):
                hinned.append(int(grade))
                
            average = sum(hinned) / len(hinned)  
            print(f"Õpilase {nimi} keskmine hinne: {average:.2f}")
            return
    print(f"Õpilast nimega '{nimi}' ei leitud.")

