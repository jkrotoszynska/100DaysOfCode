from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.place(x=100, y=150)
my_label["text"] = "New Text"


def button_clicked():
    my_label.config(text=entry.get())
button = Button(text="Click me", command=button_clicked)
button.place(x=0, y=0)


entry = Entry(width=30)
entry.place(x=100, y=0)


window.mainloop()