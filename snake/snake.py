from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.x = 0
        self.create_snake()




    def create_snake(self):

        segments = []
        for i in range(3):
            n = Turtle()
            n.color("white")
            n.shape("square")
            n.penup()
            n.goto(self.x, 0)
            self.x -= 20
            self.segments.append(n)


    def add_segment(self):

        n = Turtle()
        n.color("white")
        n.shape("square")
        n.penup()
        n.goto(self.x, 0)
        self.x -= 20
        self.segments.append(n)

    def reset(self):

        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()




    def move(self):

        for num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num - 1].xcor()
            new_y = self.segments[num - 1].ycor()
            self.segments[num].goto(new_x, new_y)

        self.segments[0].forward(20)
        self.head = self.segments[0]

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(180)

    def left(self):
        self.segments[0].setheading(0)









