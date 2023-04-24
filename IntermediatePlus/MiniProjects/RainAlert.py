import requests

API_KEY = ""
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

location_params = {
    "lat": 54.3521,
    "lon": 18.6464,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(OWM_Endpoint, params = location_params)

response.raise_for_status()
weather_data = response.json()
weather_hourly = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_hourly:
    id = hour_data["weather"][0]["id"]
    if int(id) < 700:
        #print("Bring an umbrella")
        will_rain = True

if will_rain:
    print("Bring an umbrella")
