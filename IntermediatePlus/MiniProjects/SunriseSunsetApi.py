import requests

MY_LAT = 54.352024
MY_LONG = 18.646639

coordinates = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=coordinates)

response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0:2]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0:2]

print(f"Sunrise: {sunrise} \nSunset: {sunset}")
