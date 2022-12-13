from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = None


# ---------------------------- WORDS GENERATOR ------------------------------- #
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_img, image=front_img)
    window.after(3000, func=flip_card)

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_img, image=back_img)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)

title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, columnspan=2, row=0)


yes_img = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_img, highlightthickness=0, command=next_card)
yes_button.config(pady=50)
no_img = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_img, highlightthickness=0, command=next_card)
no_button.config(pady=50)
yes_button.grid(column=1, row=1)
no_button.grid(column=0, row=1)

next_card()

window.mainloop()