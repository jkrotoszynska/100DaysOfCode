from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
email_user = Entry(width=43)
email_user.grid(row=2, column=1, columnspan=2, sticky="E")
password = Entry(width=24)
password.grid(row=3, column=1, sticky="E")


#Buttons
generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2, sticky="W")
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="E")


window.mainloop()