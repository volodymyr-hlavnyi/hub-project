
import requests
import sys


def ls46_1(name_site: str = 'https://example.com'):
    arg = sys.argv
    if len(arg) < 2:
        print('You should setup file name for running in cmd line')
    else:
        name_site = arg[1]
    response = requests.get(f"{name_site}")
    if response.status_code == 200:
        print(f"Site: {name_site} is available")
    else:
        print(f"Site: {name_site} is not available")


def get_lat_lon(city_name):
    api_key = "YOUR_API_KEY"
    geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"

    response = requests.get(geocoding_url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Check if we got any results
        if data:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return latitude, longitude
        else:
            print(data.reason)
            return None, None
    else:
        print(response.reason)
        return None, None


def get_weather_by_city(city_name):
    name_site = 'https://open-meteo.com/'
    response = requests.get(f"{name_site}")
    if response.status_code == 200:
        print(f"Site: {name_site} is available")
    else:
        print(f"Site: {name_site} is not available")

    latitude, longitude = get_lat_lon(city_name)
    print(f"City: {city_name} Latitude: {latitude}, Longitude: {longitude}")
    if not latitude and not longitude:
        return print(f"Can't get weather data for {city_name}")
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None



if __name__ == '__main__':

    # ls46_1()

    city_name = "New York"
    weather_data = get_weather_by_city(city_name)
    if weather_data:
        print("Weather data for", city_name)
        for k,v in weather_data.items():
            print(f"{k}: {v}")
    else:
        print("Failed to retrieve weather data.")