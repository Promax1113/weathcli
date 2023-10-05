import requests


#finds more or less where user resides 

def get_location():
    location_api = 'https://ipapi.co/json/'
    response = requests.get(location_api)

    if response.status_code == 200:
        longitude = response.json()["longitude"]
        latitude =  response.json()["latitude"]

        return {"longitude" : longitude , "latitude" : latitude, "city": response.json()['city']}

    else:
        print('\nToo many requests!\n')
        exit(0)
    


def weather_info(coordinates: dict = None):
    if not coordinates:
        location = get_location() 
        longitude = location["longitude"]
        latitude = location["latitude"]
    else:
        longitude = coordinates['longitude']
        latitude = coordinates['latitude']
    weather_api = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    weather_response = requests.get(weather_api)

    if weather_response.status_code == 200:
        return weather_response.json()
 
    else:
        print('\nToo many requests!\n')
        exit(0)
    
    







