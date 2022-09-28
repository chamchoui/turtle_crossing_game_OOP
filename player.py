from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90) # head north only

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        #move paces of turtle by 10
        self.forward(MOVE_DISTANCE)

    #check if player already at finish
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y: # use the turtle ycordinate
            return True
        else:
            return False
