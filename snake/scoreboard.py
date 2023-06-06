from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.s = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 300)
        self.color("white")
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score: {self.s} High Score: {self.high_score}", align="center", font=("Aria", 24, "normal"))


    def increase(self):
        self.s +=1
        self.clear()
        self.update()

    def reset(self):
        if self.s > self.high_score:
            self.high_score = self.s
            with open("data.txt","w") as data:
                data.write(f"{self.high_score}")
        self.s = 0
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Aria", 24, "normal"))




