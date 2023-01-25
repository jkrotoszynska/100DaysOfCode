import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()

MY_EMAIL = ""
PASSWORD = ""
SECOND_EMAIL = "" 

if day_of_week == 2:
    with open("quotes.txt") as file:
        contents = file.readlines()
        quote = random.choice(contents)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() 
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=SECOND_EMAIL, 
            msg=f"Subject:Monday Motivation\n\n{quote}")
