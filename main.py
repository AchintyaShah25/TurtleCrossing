import time
from turtle import Screen
from player import Player
from car import Car
from score import Score
player = Player()
screen = Screen()
car = Car()
score = Score()
screen.title("Achintya's Turtle crossing")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(player.up, "Up")
game = True
while game:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    car.move()
    if player.otherside():
        car.car_speed()
        score.level_up()
    for ca in car.cars:
        if ca.distance(player) < 20:
            game = False
            score.sco()
            score.gameover()

screen.exitonclick()