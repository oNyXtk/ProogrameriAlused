

import re

def parse_weather_data(weather_data):
    
    forecasts = []
    raw_forecasts = weather_data.split('---')
    
    for forecast in raw_forecasts:
        if forecast.strip():  
            date = re.search(r'Kuupäev:\s*(\d{2}\.\d{2}\.\d{4})', forecast)
            temperature = re.search(r'Temperatuur:\s*(-?\d+)°C', forecast)
            precipitation = re.search(r'Sademed:\s*(\w+)', forecast)
            
            if date and temperature and precipitation:
                forecasts.append({
                    'date': date.group(1),
                    'temperature': int(temperature.group(1)),
                    'precipitation': precipitation.group(1)
                })
    
    return forecasts

def find_coldest_day(forecasts):
    
    coldest_day = min(forecasts, key=lambda x: x['temperature'])
    return coldest_day

def count_precipitation_days(forecasts, precip_type):
   
    count = sum(1 for forecast in forecasts if forecast['precipitation'].lower() == precip_type.lower())
    return count
