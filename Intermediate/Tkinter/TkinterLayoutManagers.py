from tkinter import *

#pack(left or right or bottom), place(x,y), grid(column, row)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=100)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)
my_label["text"] = "New Text"
my_label.config(padx=50)


def button_clicked():
    my_label.config(text=entry.get())
button = Button(text="Click me", command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text="Click me, please", command=button_clicked)
new_button.grid(column=2,row=0)


entry = Entry(width=30)
entry.grid(column=3,row=2)

window.mainloop()