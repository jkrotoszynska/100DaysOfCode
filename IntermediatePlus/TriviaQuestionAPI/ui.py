from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text", 
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="./images/true.png")
        true_button = Button(image=true_button_img, highlightthickness=0)
        true_button.grid(column=0, row=2)

        false_button_img = PhotoImage(file="./images/false.png")
        false_button = Button(image=false_button_img, highlightthickness=0)
        false_button.grid(column=1, row=2)

        score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)