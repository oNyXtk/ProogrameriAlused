class MurderStatsManager():
    def __init__(self):
        self.data = {}
    def add_data(self, continent, country, city, count):
        if continent in self.data and country in self.data[continent] and city in self.data[continent][country]:
            self.data[continent][country][city] = count
                                
    def get_stats(self):
        for path, value in self.data.items():
            print(path)
            print(value)
stats = MurderStatsManager()
stats.data = {
    "Europe": {
        "Estonia": {
            "Tallinn": 5
        },
        "Finland": {
            "Helsinki": 3
        }
    },
    "Asia": {
        "Japan": {
            "Tokyo": 8
        }
    }
}