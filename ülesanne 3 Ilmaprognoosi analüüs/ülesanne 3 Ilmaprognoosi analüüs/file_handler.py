

def read_weather_data(file_path):
    
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data
