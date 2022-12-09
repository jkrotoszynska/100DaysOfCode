from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=400, height=300)
window.config(padx=100, pady=50)

miles = Label(text="Miles", font=("Arial", 20))
miles.grid(column=2,row=0)

equal = Label(text="is equal to", font=("Arial", 20))
equal.grid(column=0,row=1)

km = Label(text="Km", font=("Arial", 20))
km.grid(column=2,row=1)

def button_clicked():
    km_value.config(text=float(miles_value.get()) * 1.6)
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)

miles_value = Entry(width=10)
miles_value.grid(column=1,row=0)

km_value = Label(text="0", font=("Arial", 20))
km_value.grid(column=1,row=1)

window.mainloop()