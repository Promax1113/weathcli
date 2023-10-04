import requests


#finds more or less where user resides 

def get_location():
    location_api = 'https://ipapi.co/json/'
    response = requests.get(location_api)

    if response.status_code == 200:
        longitude = response.json()["longitude"]
        latitude =  response.json()["latitude"]

        coordinates = {"longitude" : longitude , "latitude" : latitude}

    else:
        print(f"error{response.status_code}")
    
    return coordinates

def weather_info():
    location = get_location() 

    longitude = location["longitude"]

    latitude = location["latitude"]

    weather_api = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"

    weather_response = requests.get(weather_api)

    if weather_response.status_code == 200:
        print(weather_response.json())
 
    else:
        print(f"error: {weather_response.status_code}")
    
    return weather_info

print(get_location())

#print(weather_info())







