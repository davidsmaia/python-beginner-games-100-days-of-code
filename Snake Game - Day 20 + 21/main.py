from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") #screen color
screen.title("My Snake Game")
screen.tracer(0)

# TODO -> Create 3 turtles and position them like the video.
#      -> Eache turtle should be a white square (default size: 20x20).

starting_x_positions = [0, -20, -40] #Y is already 0

segments = []

# For loop that creates the snake by segment -> 3 in this case
for turtle_index in range(3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup() #to not draw a line on the screen. The square will still be created
    new_segment.setx(starting_x_positions[turtle_index])
    segments.append(new_segment)

# print(segments)

# While loop to maintain tha game on
game_is_on = True
while game_is_on:
    screen.update() #updates the graphics only after the 3 pieces moves
    time.sleep(0.1)

    # For loop to move the Snake. Last segment to first segment
    # The segment 3 goes to the position of the segment 2, segment 2 goes to the position of the segment 1...
    for seg_num in range(len(segments) - 1, 0,-1): #start, stop, step. Starting from the last segment
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20) #segment 1 go forward.

screen.exitonclick() # hold the screen until we click to close
