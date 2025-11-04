# SNAKE GAME

A Turtle Crossing Game implementation in Python, developed during the course: *[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/?srsltid=AfmBOor9MN3qCpzSHSlwpW-iGIEaZoRj4bMQ1rHAaDoqW5OMJrucjWH5)*

This project was created on the day 23.

## How the Game Play Works

 - A turtle moves forwards when the "Up" key is pressed.
 - Cars are randomly generated along the y-axis and moves from one edge of the screen to another.
 - When the turtle hits the top edge of the screen, it moves back to the original position and 1 point is added to the scoreboard
 - The cars speed increases with the points.
 - When the turtle collides with a car, it's Game Over.

## Controls

    ↑ - Move Up

## Technologies Used

 - **Python 3.13**
 - **Turtle Graphics**: For game visualization and graphics
 - **Time Module**: For game timing and control
 - **Random Module**: For car's colors and positions

## Project Structure

Turtle Crossing Game - Day 23/

├── main.py # Main game file

├── car_manager.py # Cars functionalities

├── player.py # Turtle controlled by the player

├── scoreboard.py # Scoreboard generator

├── road_line.py # Center road lines

├── turtle-crossing-start.zip # Initial files provided by Angela Yu

└── README.md # Project documentation