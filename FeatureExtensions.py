class MurderStatsManager:
    def __init__(self):
        self.data = {}

    def add_data(self, continent, country, city, count):
        if continent not in self.data:
            self.data[continent] = {}
        if country not in self.data[continent]:
            self.data[continent][country] = {}
        self.data[continent][country][city] = count

    def get_stats(self):
        return self.data

    def get_city_stats(self, continent, country, city):
        try:
            return self.data[continent][country][city]
        except KeyError:
            return f"Data for {city} not found."

    def remove_city(self, continent, country, city):
        try:
            del self.data[continent][country][city]
        except KeyError:
            return f"Data for {city} not found."
        
    def add_africa_data(self):
        self.add_data("Africa", "South Africa", "Cape Town", 12)
        self.add_data("Africa", "Nigeria", "Lagos", 15)

manager = MurderStatsManager()
manager.add_data("Europe", "Estonia", "Tallinn", 5)
manager.add_data("Europe", "Finland", "Helsinki", 3)
manager.add_data("Asia", "Japan", "Tokyo", 8)

print(manager.get_stats()) 
