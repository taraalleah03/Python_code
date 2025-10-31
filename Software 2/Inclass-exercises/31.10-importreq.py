import requests, json

keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.tvmaze.com/search/shows?q=" + keyword
#response = requests.get(request).json()
#print(response)

#print(json.dumps(response, indent=2))

#for a in response:
#   print(a["show"]["name"])

#print(response[0]["show"]["name"])

try:
    response = requests.get(request)
    if response.status_code==200:
        json_string = response.json()
        # print(json.dumps(json_response, indent=2))
        for a in json_string:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")