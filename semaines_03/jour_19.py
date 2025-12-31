# Weather App using OpenWeatherMap API
import requests

# Step 1: API Setup
API_KEY = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Step 2: Function to get weather data
def get_weather(city):
    try:
        # Construct the complete API URL
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        
        # Make a GET request to fetch the raw HTML content
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            weather = {
                'City': data['name'],   
                'Temperature': f"{data['main']['temp']}C",
                'Weather': data['weather'][0]['description'].title(),
                'Humidity': f"{data['main']['humidity']}%",
                'Wind Speed': f"{data['wind']['speed']} m/s"
            }
            return weather
        elif response.status_code == 404:
            print("Error: City not found.")
        else:
            print("Error: Unable to fetch data from the API.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

# Step 3: Display weather Information
def display_weather(weather):
    print("\n--- Weather Information ---")
    for key, value in weather.items():
        print(f"{key}: {value}")
    print("---------------------------\n")

# Step 4: Main Program loop
def main():
    while True:
        print("\n--- Weather App ---")
        city = input("Enter city name (or 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            break
        weather = get_weather(city)
        if weather:
            display_weather(weather)
