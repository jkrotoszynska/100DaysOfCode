from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        canvas = Canvas(width=300, height=250)
        quote_text = canvas.create_text(150, 207, text="HERE", width=250, font=("Arial", 16, "bold"), fill="white")
        canvas.grid(row=1, column=0, columnspan=2)

        true_button_img = PhotoImage(file="./images/true.png")
        true_button = Button(image=true_button_img, highlightthickness=0)
        true_button.grid(column=0, row=2)

        false_button_img = PhotoImage(file="./images/false.png")
        false_button = Button(image=false_button_img, highlightthickness=0)
        false_button.grid(column=1, row=2)

        score = Label(text="score", font=("Arial", 16, "bold"))
        score.grid(column=1, row=0)

        self.window.mainloop()