from turtle import Turtle
import random

# here is the fundamental need to be strong

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6) #randomize the car generation
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y_axis = random.randint(-250, 250) #set random starting car position
            new_car.goto(300, random_y_axis)
            self.all_car.append(new_car)

    def move_car(self):
        for car in self.all_car:
            car.backward(self.car_speed)
            #reduce no# car made

    def level_up(self):
        #increase car speed once success cross
        self.car_speed += MOVE_INCREMENT