from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.score_increase = 1
        with open("data.txt") as data:
            self.highscore = int(data.read())

    def current_score(self):
        self.ht()
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score} High Score: {self.highscore}", True, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
                self.highscore = self.score
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        if self.score == 0:
            self.current_score()
        self.score += self.score_increase
        self.current_score()
