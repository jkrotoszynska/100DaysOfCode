from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles = Label(text="Miles")
miles.grid(column=2,row=0)

equal = Label(text="is equal to")
equal.grid(column=0,row=1)

km = Label(text="Km")
km.grid(column=2,row=1)

def miles_to_km():
    km_value.config(text=float(miles_value.get()) * 1.609)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1,row=2)

miles_value = Entry(width=10)
miles_value.grid(column=1,row=0)

km_value = Label(text="0")
km_value.grid(column=1,row=1)

window.mainloop()