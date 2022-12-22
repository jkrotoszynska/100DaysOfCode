import smtplib

my_email = ""
password = "" # need to generate password for new app

connection = smtplib.SMTP("smtp.gamil.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addres="", msg="Hello")
connection.close()