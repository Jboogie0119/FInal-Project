import requests
import json

def get_weather(api_key, city):
    ##fethes weather data from the OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def main():
    api_key = 'your_api_key_here'  # Replaces your OpenWeatherMap API key
    city = 'London'  # This is an example city

    weather_data = get_weather(api_key, city)
    
    # Manipulates and extracts the JSON info
    temp = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']

    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {weather_description}")
    print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    main()
