import requests

APIkey = "410e96ec235ace893f1c0bad0070534f"

municipality = input("Enter Municipality: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={APIkey}"
response = requests.get(url).json()