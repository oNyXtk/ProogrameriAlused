
class Person:
    def __init__(self, name, age, salary, city):
        self.name = name
        self.age = age
        self.salary = salary
        self.city = city
        self.tax_paid = 0

    def pay_taxes(self):
        tax = self.salary * 0.2  
        self.city.budget += tax
        self.tax_paid += tax
        print(f"{self.name} paid {tax} in taxes to {self.city.name}.")

    def move_to_city(self, new_city):
        print(f"{self.name} is moving from {self.city.name} to {new_city.name}")
        self.city.remove_resident(self)
        new_city.add_resident(self)
        self.city = new_city


class City:
    def __init__(self, name, population, budget, county):
        self.name = name
        self.population = population
        self.budget = budget
        self.residents = []
        self.county = county

    def add_resident(self, person):
        self.residents.append(person)
        self.population += 1

    def remove_resident(self, person):
        if person in self.residents:
            self.residents.remove(person)
            self.population -= 1

    def collect_taxes(self):
        for resident in self.residents:
            resident.pay_taxes()

    def request_funding(self, amount):
        print(f"{self.name} is requesting {amount} funding from {self.county.name}")
        self.county.process_city_request(self, amount)

    def receive_funding(self, amount):
        self.budget += amount
        print(f"{self.name} received {amount} funding. New budget: {self.budget}")

    def get_info(self):
        return f"City: {self.name}, Population: {self.population}, Budget: {self.budget}"



class County:
    def __init__(self, name, area, population, budget, country):
        self.name = name
        self.area = area
        self.population = population
        self.budget = budget
        self.cities = []
        self.country = country

    def add_city(self, city):
        self.cities.append(city)
        self.population += city.population

    def collect_taxes(self):
        for city in self.cities:
            city.collect_taxes()

    def process_city_request(self, city, amount):
        if self.budget >= amount:
            self.budget -= amount
            city.receive_funding(amount)
        else:
            print(f"{self.name} doesn't have enough budget. Requesting from country.")
            self.request_government_support(amount, city)

    def request_government_support(self, amount, city):
        self.country.approve_funding(self, amount, city)

    def get_budget(self):
        return self.budget



class Country:
    def __init__(self, name, population, area, currency, language, tax_rate, budget, leader, capital):
        self.name = name
        self.population = population
        self.area = area
        self.currency = currency
        self.language = language
        self.tax_rate = tax_rate
        self.budget = budget
        self.leader = leader
        self.capital = capital
        self.counties = []

    def add_county(self, county):
        self.counties.append(county)
        self.population += county.population

    def collect_taxes(self):
        for county in self.counties:
            county.collect_taxes()

    def approve_funding(self, county, amount, city):
        if self.budget >= amount:
            self.budget -= amount
            county.budget += amount
            county.process_city_request(city, amount)
            print(f"{self.name} approved {amount} funding to {county.name} for {city.name}")
        else:
            print(f"{self.name} has insufficient budget to fund {county.name}")

    def get_budget(self):
        return self.budget

country1 = Country("Estonia", 0, 45000, "Euro", "Estonian", 0.2, 100000, "President", "Tallinn")
country2 = Country("Finland", 0, 50000, "Euro", "Finnish", 0.2, 120000, "President", "Helsinki")


county1 = County("Harjumaa", 2000, 0, 50000, country1)
county2 = County("Tartumaa", 1500, 0, 30000, country1)
county3 = County("Uusimaa", 2500, 0, 40000, country2)


country1.add_county(county1)
country1.add_county(county2)
country2.add_county(county3)


city1 = City("Tallinn", 0, 20000, county1)
city2 = City("Tartu", 0, 15000, county2)
city3 = City("Narva", 0, 10000, county1)
city4 = City("Helsinki", 0, 30000, county3)
city5 = City("Espoo", 0, 25000, county3)


county1.add_city(city1)
county1.add_city(city3)
county2.add_city(city2)
county3.add_city(city4)
county3.add_city(city5)


person1 = Person("Alice", 30, 2000, city1)
person2 = Person("Bob", 28, 1800, city1)
person3 = Person("Charlie", 40, 2200, city2)
person4 = Person("Diana", 35, 2500, city4)
person5 = Person("Eve", 32, 2400, city5)


city1.add_resident(person1)
city1.add_resident(person2)
city2.add_resident(person3)
city4.add_resident(person4)
city5.add_resident(person5)


print("\n--- Tax Collection ---")
country1.collect_taxes()
country2.collect_taxes()


print("\n--- City Funding Requests ---")
city1.request_funding(5000)
city2.request_funding(7000)


print("\n--- People Moving ---")
person1.move_to_city(city2)  
person5.move_to_city(city4)  

print("\n--- Budgets ---")
print(f"{country1.name} Budget: {country1.get_budget()}")
print(f"{county1.name} Budget: {county1.get_budget()}")
print(f"{county2.name} Budget: {county2.get_budget()}")
print(f"{city1.get_info()}")
print(f"{city2.get_info()}")
print(f"{city4.get_info()}")
print(f"{city5.get_info()}")
