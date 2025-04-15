from datetime import datetime

# Represents a single event related to a case
class Event:
    def __init__(self, note, officer_name):
        self.timestamp = datetime.now()
        self.note = note
        self.officer_name = officer_name

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.officer_name}: {self.note}"

# Represents a police case
class Case:
    def __init__(self, case_id, description):
        self.case_id = case_id
        self.description = description
        self.status = "open"
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def close_case(self):
        self.status = "closed"

    def get_timeline(self):
        return [str(event) for event in self.events]

    def get_status(self):
        return self.status

    def get_description(self):
        return self.description

    def get_case_id(self):
        return self.case_id

# Represents a police officer
class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number
        self.cases = []

    def assign_case(self, case):
        self.cases.append(case)

    def get_case_by_id(self, case_id):
        for case in self.cases:
            if case.get_case_id() == case_id:
                return case
        return None

    def get_summary(self):
        open_cases = sum(1 for case in self.cases if case.get_status() == "open")
        closed_cases = sum(1 for case in self.cases if case.get_status() == "closed")
        return f"Open cases: {open_cases}, Closed cases: {closed_cases}"

    def get_info(self):
        return f"{self.name}, Badge #{self.badge_number}"

# Simple text menu for interaction
def main():
    officer = PoliceOfficer("John Smith", "12345")
    case_id_counter = 1

    while True:
        print("\n1. Assign new case")
        print("2. Add event to case")
        print("3. Close case")
        print("4. Show all cases")
        print("5. Show case timeline")
        print("6. Officer summary")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            desc = input("Case description: ")
            case = Case(case_id_counter, desc)
            officer.assign_case(case)
            print(f"Case #{case_id_counter} assigned.")
            case_id_counter += 1

        elif choice == "2":
            try:
                cid = int(input("Case ID: "))
                case = officer.get_case_by_id(cid)
                if case:
                    note = input("Event note: ")
                    event = Event(note, officer.name)
                    case.add_event(event)
                    print("Event added.")
                else:
                    print("Case not found.")
            except ValueError:
                print("Invalid ID format.")

        elif choice == "3":
            try:
                cid = int(input("Case ID: "))
                case = officer.get_case_by_id(cid)
                if case:
                    case.close_case()
                    print("Case closed.")
                else:
                    print("Case not found.")
            except ValueError:
                print("Invalid ID format.")

        elif choice == "4":
            for case in officer.cases:
                print(f"ID: {case.get_case_id()}, Status: {case.get_status()}, Description: {case.get_description()}")

        elif choice == "5":
            try:
                cid = int(input("Case ID: "))
                case = officer.get_case_by_id(cid)
                if case:
                    print("Case timeline:")
                    for event in case.get_timeline():
                        print(event)
                else:
                    print("Case not found.")
            except ValueError:
                print("Invalid ID format.")

        elif choice == "6":
            print(officer.get_info())
            print(officer.get_summary())

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

main()
