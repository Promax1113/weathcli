import requests

api = 'https://ipapi.co/json/'
response = requests.get(api)

if response.status_code == 200:
    longitude = print(response.json()["longitude"])
    latitude = print(response.json()["latitude"])

    coordinates = {"longitude":longitude , "latitude" : latitude}

else:
    print(f"error{response.status_code}")