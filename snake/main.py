from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import  Score
import time


screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)


score = Score()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.right, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "d")






game = True

while game == True:
    screen.update()
    time.sleep(0.08)

    snake.move()



    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.add_segment()

    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        score.reset()
        score.game_over()
        game = False


    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            score.game_over()
            game = False



screen.exitonclick()
