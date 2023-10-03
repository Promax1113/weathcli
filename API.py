import requests


#finds more or less where user resides 
location_api = 'https://ipapi.co/json/'
response = requests.get(location_api)

if response.status_code == 200:
    longitude = print(response.json()["longitude"])
    latitude = print(response.json()["latitude"])

    coordinates = {"longitude":longitude , "latitude" : latitude}

else:
    print(f"error{response.status_code}")

weather_api = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
weather_response = requests.get(weather_api)

if weather_response.status_code == 200:
    print(weather_response.json())

else:
    print(f"error:{weather_response.status_code}")


