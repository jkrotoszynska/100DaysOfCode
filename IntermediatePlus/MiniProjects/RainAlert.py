import os
from twilio.rest import Client
import requests

API_KEY = ""
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

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
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella!",
        from_=['TWILIO_NUMBER'],
        to=['MY_NUMBER']
        )
    
    print(message.status)
