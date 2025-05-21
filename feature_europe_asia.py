class MurderStatsManager():
    def __init__(self):
        self.data = {}
    def add_data(self, continent, country, city, count):
        for path, value in self.data.items():
            if path == continent:        
                for path2 , value2 in value.items():
                    if path2 == country: 
                        for path3 , value3 in value2.items():
                            if path3 == city:
                                value2[path3] = count  
                                return
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