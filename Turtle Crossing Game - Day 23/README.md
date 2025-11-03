# SNAKE GAME

A Turtle Crossing Game implementation in Python, developed during the course: *[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/?srsltid=AfmBOor9MN3qCpzSHSlwpW-iGIEaZoRj4bMQ1rHAaDoqW5OMJrucjWH5)*

This project was created on the day 23.

## How the Game Play Works

 - A turtle moves forwards when the "Up" key is pressed.
 - Cars are randomly generated along the y-axis and moves from the right edge of the screen to the left edge.
 - When the turtle hits the top edge of the screen, it moves back to the original position and adds 1 point to the scoreboard
 - The car speed increases with the points.
 - When the turtle collides with a car, it's Game Over.

## Controls

    ↑ - Move Up

## Technologies Used

 - **Python 3.13**
 - **Turtle Graphics**: For game visualization and graphics
 - **Time Module**: For game timing and control

## Project Structure

Turtle Crossing Game - Day 23/

├── main.py # Main game file

├── car_manager.py # Cars functionalities file 

├── player.py # Turtle controlled by the player file

├── scoreboard.py # Scoreboard file

└── README.md # Project documentation