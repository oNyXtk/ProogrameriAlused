

from file_handler import read_weather_data
from weather_analyzer import parse_weather_data, find_coldest_day, count_precipitation_days

def main():
    
    weather_data = read_weather_data('weather.txt')
    
   
    forecasts = parse_weather_data(weather_data)
    
    
    print("Kõik ilmaprognoosi andmed:")
    for forecast in forecasts:
        print(f"Kuupäev: {forecast['date']}, Temperatuur: {forecast['temperature']}°C, Sademed: {forecast['precipitation']}")
    
    
    coldest_day = find_coldest_day(forecasts)
    print(f"\nKõige külmem päev on {coldest_day['date']} temperatuuriga {coldest_day['temperature']}°C.")
    
   
    rain_count = count_precipitation_days(forecasts, 'vihm')
    snow_count = count_precipitation_days(forecasts, 'lumi')
    print(f"\nPäevade arv, kus sadas vihma: {rain_count}")
    print(f"Päevade arv, kus sadas lund: {snow_count}")
    
    main()
