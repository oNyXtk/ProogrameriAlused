from grades_manager import add_student, view_students, search_student, calculate_average
from file_handler import read_grades, write_grades

def main():
    while True:
        print("\nÕpilaste hinded")
        print("1. Lisa õpilane ja hinnet")
        print("2. Vaata kõiki õpilasi ja nende hindeid")
        print("3. Otsi õpilast nime järgi")
        print("4. Arvuta õpilase keskmine hinne")
        print("5. Välju")

        choice = input("Vali toiming (1-5): ")

        if choice == '1':
            nimi = input("Sisesta õpilase nimi: ")
            hinned = input("Sisesta hinded (eralda komadega): ").split(',')
           
            add_student(nimi, [int(hind) for hind in hinned])
        elif choice == '2':
            view_students()  
        elif choice == '3':
            nimi = input("Sisesta õpilase nimi: ")
            search_student(nimi)  
        elif choice == '4':
            nimi = input("Sisesta õpilase nimi: ")
            calculate_average(nimi)  
        elif choice == '5':
            break  
        else:
            print("Vale sisend, proovi uuesti.")  
main()
