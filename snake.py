from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)
    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment)-1 , 0, -1):
            new_x= self.segment[seg_num-1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)

