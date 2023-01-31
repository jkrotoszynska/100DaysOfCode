from xmlrpc.client import DateTime
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 54.352024
MY_LONG = 18.646639
MY_EMAIL = 
PASSWORD =
SECOND_EMAIL = 

def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_latitude = data["iss_position"]["latitude"]
    iss_longitude = data["iss_position"]["longitude"]

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():

    coordinates = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=coordinates)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    
    time.sleep(60)

    if is_iss_overhead() and is_night():
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() 
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=SECOND_EMAIL, 
                msg="Subject:ISS NOW\n\nLook up!.")
