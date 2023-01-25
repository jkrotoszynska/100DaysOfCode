import smtplib
from datetime import datetime
import random
import pandas

today = datetime.now()
today_tuple = (today.month, today.day)

PLACEHOLDER = "[NAME]"
MY_EMAIL = ""
PASSWORD = ""
SECOND_EMAIL = "" 
LETTERS = ["letter_1.txt","letter_2.txt","letter_3.txt"]

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as file:
        contents = file.read()
        wishes = contents.replace(PLACEHOLDER, birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() 
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=SECOND_EMAIL, 
            msg=f"Subject:Happy Birthday! \n\n{wishes}")



