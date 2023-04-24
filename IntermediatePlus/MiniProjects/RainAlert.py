import requests

API_KEY = ""
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

location_params = {
    "lat": 54.3521,
    "lon": 18.6464,
    "appid": API_KEY
}

response = requests.get(OWM_Endpoint, params = location_params)

print(response.status_code)
print(response.json())