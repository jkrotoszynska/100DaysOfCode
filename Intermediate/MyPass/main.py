from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- SEARCH DATA ------------------------------- #
def find_password():
    website_data = website.get()
    if len(website_data) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left field empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
        else:
            if website_data in data:
                email = data[website_data]["email"]
                password = data[website_data]["password"]
                messagebox.showinfo(title=f"{website_data}", message=f"Email:{email} \nPassword:{password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website_data} exists.")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():

    password.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8,10))]
    password_number = [choice(numbers) for _ in range(randint(2,4))]
    password_symbol = [choice(symbols) for _ in range(randint(2,4))]

    password_list = password_letter + password_number + password_symbol
    shuffle(password_list)

    new_password = "".join(password_list)
    password.insert(0, new_password)
    pyperclip.copy(new_password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_data = website.get()
    email_user_data = email_user.get()
    password_data = password.get()
    new_data = {
        website_data: {
            "email": email_user_data,
            "password": password_data
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)
    
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#Entry
website = Entry(width=43)
website.grid(row=1, column=1, columnspan=2, sticky="E")
website.focus()
email_user = Entry(width=43)
email_user.grid(row=2, column=1, columnspan=2, sticky="E")
email_user.insert(0, "justyna@email.com")
password = Entry(width=24)
password.grid(row=3, column=1, sticky="E")


#Buttons
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2, sticky="W")
generate_button = Button(text="Generate Password", width=15, command=generate)
generate_button.grid(row=3, column=2, sticky="W")
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="E")


window.mainloop()