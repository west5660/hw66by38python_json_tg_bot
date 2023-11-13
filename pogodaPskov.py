import requests

def get_weather():
    key = 'ffba57f44fa1889286e1e5a405e4e879'
    zapros = 'https://api.openweathermap.org/data/2.5/weather'
    id = 504341

    try:
        result = requests.get(zapros, params={'id': id, 'lang': 'ru', 'units': 'metric', 'appid': key})
        data = result.json()
        k1 = data.get('name')
        k2 = str(round(data['main']['temp'], 1)) + 'C'
        k3 = str(data['wind']['speed']) + 'm/s'
        k4 = data['weather'][0]['description']
        pogoda_info = f"{k1}, Температура: {k2}, Скорость ветра: {k3}, Описание: {k4}"
        return pogoda_info
    except:
        return 'Не удалось получить информацию о погоде'

import requests

def get_forecast():
    key = 'ffba57f44fa1889286e1e5a405e4e879'
    zapros = 'https://api.openweathermap.org/data/2.5/forecast'
    id = 504341

    try:
        result = requests.get(zapros, params={'id': id, 'lang': 'ru', 'units': 'metric', 'appid': key})
        data = result.json()
        forecast_data = []
        for i in data['list']:
            if i['dt_txt'][11:13] == '15':
                temp = i['main']['temp']
                description = i['weather'][0]['description']
                dt_txt = i['dt_txt']
                forecast_data.append({'temp': temp, 'description': description, 'dt_txt': dt_txt})
        return forecast_data
    except:
        return 'Не удалось получить прогноз погоды'
