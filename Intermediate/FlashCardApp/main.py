from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = None


# ---------------------------- WORDS GENERATOR ------------------------------- #
data = pandas.read_csv("data/french_words.csv")
french_words = data["French"]

def generate():
    random_word = random.choice(french_words)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=random_word)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=img)

title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, columnspan=2, row=0)


yes_img = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_img, highlightthickness=0, command=generate)
yes_button.config(pady=50)
no_img = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_img, highlightthickness=0, command=generate)
no_button.config(pady=50)
yes_button.grid(column=1, row=1)
no_button.grid(column=0, row=1)

generate()

window.mainloop()