from tkinter import *

#Creating a new window and config
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Labels
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"

#Button
def button_clicked():
    my_label.config(text=entry.get())

button = Button(text="Click me", command=button_clicked)
button.pack()

#Entry
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with...")
entry.pack()

#Text
text = Text(height=5,width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_ = 0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
#Radiobutton
#Listbox

window.mainloop()