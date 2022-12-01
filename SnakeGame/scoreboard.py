from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.goto(0,250)
        self.penup()
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                    file.write(f"\n{self.score}")
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def new_high_score(self):
        with open("data.txt", mode="a") as file:
            the_highest = file.read()
            if the_highest < self.score:
                file.write(f"\n{self.high_score}")

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()