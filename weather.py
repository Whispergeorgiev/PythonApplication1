import requests

city = input("Enter a city:")
url = "http://api.weatherapi.com/v1/current.json?key=c228279768b1475cb99111206231611&q="+city+"&aqi=no"
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get("current").get("temp_c")
describtion = weather_json.get("current").get("condition").get("text")

print("Today weather in", city, "is", describtion, "and", temp, "degrees")

