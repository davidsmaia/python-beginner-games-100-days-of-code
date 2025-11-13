# TODO Extract all the Snake Related Functionalities from main.py
from turtle import Turtle

# Global variables
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] # attribute created because the very first segment will always be used to move the snake

    #create_snake() + add_segment() combined in fact creates the snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()  # to not draw a line on the screen. The square will still be created
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Remove all segments that was added on the snake -> It's been used when the snake hits the wall
    def reset(self):
        for seg in self.segments: #makes the segments disappear from the screen
            seg.goto(1000,1000)
        self.segments.clear() #clear the segments list
        self.create_snake() #create another 3 new segments again
        self.head = self.segments[0]

    # Add a new segment to the snake after it eats a food
    def extend(self):
        #getting the position of the very last segment of the snake and adding a new one on this position
        self.add_segment(self.segments[-1].position())


    # Bringing the functionality of moving the snake from main.py
    def move(self):
        # For loop to move the Snake. Last segment to first segment
        # The segment 3 goes to the position of the segment 2, segment 2 goes to the position of the segment 1...
        for seg_num in range(len(self.segments) - 1, 0,-1): #start, stop, step. Starting from the last segment
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE) #segment 1 go forward.

    # TODO Create the methods "up", "down", "left", "right" to move the snake when the arrow keys are pressed

    # IMPORTANT NOTE: All Segments follows the very first one

    # The Snake is not allowed to go to the opposite direction that's facing

    # Up must move to North (90°)
    def up(self):
        if self.head.heading() != DOWN: #the snake CAN'T go down while facing north
            # self.segments[0].setheading(90) #using the self.head attribute instead
            self.head.setheading(UP)

    # Down must move to South (270°)
    def down(self):
        if self.head.heading() != UP: #the snake CAN'T go UP while facing South
            self.head.setheading(DOWN)

    # Right must move to East (0°)
    def right(self):
        if self.head.heading() != LEFT: #the snake CAN'T go Left while facing East
            self.head.setheading(RIGHT)

    # Right must move to West (180°)
    def left(self):
        if self.head.heading() != RIGHT: #the snake CAN'T go Right while facing West
            self.head.setheading(LEFT)
