import requests

APIkey = "410e96ec235ace893f1c0bad0070534f"

municipality = input("Enter Municipality: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={APIkey}"
response = requests.get(url)

if response.status_code == 200:
    info = response.json()

    temperature = info["main"]["temp"] #this is in Kelvin
    celsius = temperature - 273.15

    print(f"Current weather in {municipality} is: {info['weather'][0]['description']}")
    print(f"Temperature in Celsius: ", celsius)

else:
    print("Error")
