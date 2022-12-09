from tkinter import *

#pack(left or right or bottom), place(x,y), grid(column, row)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)
my_label["text"] = "New Text"


def button_clicked():
    my_label.config(text=entry.get())
button = Button(text="Click me", command=button_clicked)
button.grid(column=1,row=2)


entry = Entry(width=30)
entry.grid(column=1,row=1)

window.mainloop()