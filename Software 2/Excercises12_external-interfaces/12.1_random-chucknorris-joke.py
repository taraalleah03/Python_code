import requests, json

joke = "https://api.chucknorris.io/jokes/random"
response = requests.get(joke).json()
print("Random Chuck Norris joke:\n"+ response["value"])

