import requests

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search.php"
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

HEADERS = {
    "referer": "https://nominatim.openstreetmap.org/ui/search.html"
}

def get_coordinates (city_name):
    params = {
        "q": city_name.strip(),
        "polygon_geojson": 1,
        "format": "jsonv2",
    }

    response = requests.get(NOMINATIM_URL, params=params, headers=HEADERS)

    if response.status_code == 200 and response.json():
        location = response.json()[0]
        return float(location["lat"]), float(location["lon"])
    else:
        return None, None

def get_weather (lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(OPEN_METEO_URL, params=params)
    if response.status_code == 200:
        weather = response.json()["current_weather"]
        return weather["temperature"], weather["weathercode"]
    else:
        return None, None

city = input("Digite o nome da cidade: ")
latitude, longitude = get_coordinates(city)

if latitude and longitude:
    temperature, weather_code = get_weather(latitude, longitude)
    if temperature and weather_code:
        print(f"\n-- Clima em {city} --")
        print(f"Temperatura: {temperature}°C")
        print(f"Código do Clima: {weather_code}\n")
    else:
        print("Erro ao obter informações climáticas")
else:
    print("Erro ao buscar a cidade")
