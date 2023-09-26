from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 0
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write(f"Level: {self.lvl}\t High Score: {self.high_score}", align="center", font=FONT)

    def level_up(self):
        self.lvl += 1
        self.clear()
        self.write(f"Level: {self.lvl}\t High Score: {self.high_score}", align="center", font=FONT)

    def sco(self):
        if self.lvl > self.high_score:
            self.high_score = self.lvl
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 35, "normal"))
