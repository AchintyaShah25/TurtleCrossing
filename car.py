from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car:
    def __init__(self):
        self.cars = []
        self.scar = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            cared = Turtle()
            cared.shape("square")
            cared.shapesize(1, 2)
            cared.speed("slowest")
            cared.penup()
            cared.color(random.choice(COLORS))
            cared.goto(-300, random.randrange(-260, 260, 20))
            self.cars.append(cared)

    def move(self):
        for car in self.cars:
            car.forward(self.scar)
            if car.xcor() > 350:
                self.cars.remove(car)
                car.clear()

    def car_speed(self):
        self.scar += STARTING_MOVE_DISTANCE