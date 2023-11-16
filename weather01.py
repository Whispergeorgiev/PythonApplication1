import requests
from geopy.geocoders import Nominatim

# Function to check if the input corresponds to a valid city name
def is_valid_city(city):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    return location is not None and location.raw.get("type") == "city"

# Get user input for the city
city = input("Enter a city: ")

# Check if the user input is a valid city name
if city and is_valid_city(city):
    # Make the API request
    url = f"http://api.weatherapi.com/v1/current.json?key=c228279768b1475cb99111206231611&q={city}&aqi=no"
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON data
        weather_json = response.json()

        # Check if the expected keys are present in the JSON
        current_data = weather_json.get("current", {})
        temp = current_data.get("temp_c")
        description = current_data.get("condition", {}).get("text")

        if temp is not None and description is not None:
            print(f"Today's weather in {city} is {description} and {temp} degrees Celsius.")
        else:
            print("Sorry, we couldn't retrieve complete weather data for the specified city.")
    else:
        print(f"Sorry, there was an error fetching weather data. Please check your city name and try again.")
else:
    print("Invalid input. Please enter a valid city name.")
