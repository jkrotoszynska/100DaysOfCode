import smtplib

my_email = ""
password = "" # need to generate password for new app

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #tls - transport layer security -> this line will make this connection secure
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="", 
        msg="Subject:Hello\n\nThis is the body of my email.")
