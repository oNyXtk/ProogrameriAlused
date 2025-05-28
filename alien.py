from rich.console import Console
from rich.table import Table
from time import sleep
from random import randint

console = Console()

for i in range(5, 0, -1):
    console.log(f"An alien will attack your spaceship after {i} minutes")
    sleep(1)
console.log("You are already attacked")


class CrewMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.hp = 100
        self.strength = randint(15, 30)
        self.status = True  # True means alive

    def injure(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.status = False
            console.log(f"[red]{self.name} {self.role} was killed by the Alien[/red]")
        else:
            console.log(f"[yellow]{self.role} {self.name} took {damage} damage! Left {self.hp} health points[/yellow]")

    def is_alive(self):
        return self.status


class Alien:
    def __init__(self):
        self.aggression = randint(1, 10)
        self.hp = 134
        self.status = True

    def injure_alien(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.status = False
            console.log(f"[red]Alien was killed by Crew[/red]")
        else:
            console.log(f"[yellow]Alien took {damage} damage! Left {self.hp} health points[/yellow]")

    def attack(self, crew_member):
        if self.status:
            damage = self.aggression + randint(-3, 3)
            if damage < 0:
                damage = 0
            console.log(f"Alien attacks {crew_member.role} {crew_member.name} for {damage} damage!")
            crew_member.injure(damage)

    def is_alive(self):
        return self.status


class Ship:
    def __init__(self):
        self.status = True
        self.rooms = ["Bridge", "Engine Room", "Cargo Bay", "Crew Quarters"]

    def trigger_alarm(self, room):
        console.log(f"[bold red]Alien presence detected in sector: {room}[/bold red]")

    def show_status(self):
        console.log(f"Ship status: {'Operational' if self.status else 'Destroyed'}")
        console.log(f"Rooms: {', '.join(self.rooms)}")


class Mission:
    def __init__(self, crewlist):
        self.crew = crewlist
        self.alien = Alien()
        self.ship = Ship()

    def simulate(self):
        console.log("[bold green]The mission begins[/bold green]")
        self.ship.show_status()
        sleep(1)

        for round in range(1, 10):
            console.log(f"[bold cyan]Round {round}[/bold cyan]")

            alive_crew = [member for member in self.crew if member.is_alive()]
            if not alive_crew:
                console.log("[red]All crew members are dead. Mission failed.[/red]")
                break

            target = alive_crew[randint(0, len(alive_crew) - 1)]
            self.alien.attack(target)

            
            for member in alive_crew:
                damage = member.strength + randint(-5, 5)
                if damage < 0:
                    damage = 0
                console.log(f"{member.role} {member.name} attacks Alien for {damage} damage!")
                self.alien.injure_alien(damage)
                if not self.alien.is_alive():
                    console.log("[green]Alien defeated! Mission successful![/green]")
                    self.ship.status = True
                    return

            sleep(1)

        if self.alien.is_alive():
            console.log("[red]The Alien is still alive. Mission failed.[/red]")
            self.ship.status = False

    def summary(self):
        table = Table(title="Crew members")
        table.add_column("Name", style="yellow")
        table.add_column("Role", style="green")
        table.add_column("HP", style="red")
        table.add_column("Status", style="purple")

        for crewMember in self.crew:
            status = "Alive" if crewMember.status else "Died"
            table.add_row(crewMember.name, crewMember.role, str(crewMember.hp), status)

        console.print(table)


crew = [
    CrewMember("Ripli", "Captain"),
    CrewMember("Dallas", "Sailor"),
    CrewMember("Esh", "Science officer"),
    CrewMember("Parker", "Engineer")
]

mission1 = Mission(crew)
mission1.simulate()
mission1.summary()
    