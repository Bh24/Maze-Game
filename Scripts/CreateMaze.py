##This module will create the maze
# It creates a graph and also performs depth first search on the graph
from turtle import *
from tkinter import *
from random import *

# Sets the turtle up
turtle = Turtle()

# Sets the screen up
windowMaze = turtle.getscreen()
windowMaze.title("Maze Game")

windowMaze.setup(700, 700)  # columnNums of window

turtle.speed(900)
turtle.width(3)


# Base Class
class Grid():
    def __init__(self, x, y, cellWidth, columnNum):
        self._cellWidth = cellWidth
        self._gridDim = columnNum
        self._x = x
        self._y = y

    def createRow(self):  # Creates the rows
        turtle.up()  # Won't draw the route it takes when travelling to the first co-ordinate
        turtle.goto([self._x, self._y])
        for i in range(0, self._gridDim):
            totalY = self._y + self._cellWidth  # Keeps track of which y co-ordinate it's at and draws the row of squares using the same y co-ordinate
            gridPoints.append([self._x, self._y])
            turtle.goto([self._x, self._y])
            turtle.down()  # Pen starts drawing
            turtle.goto([self._x + self._cellWidth, self._y])
            turtle.goto([self._x + self._cellWidth, totalY])
            turtle.goto([self._x, totalY])
            turtle.goto([self._x, self._y])
            self._x += self._cellWidth

        # Subclass


class BreakWall(Grid):  # Functions to create the maze
    def __init__(self, x, y, cellWidth, columnNum, colour1):
        super().__init__(x, y, cellWidth, columnNum)  # Inherits attributes from the class grid
        self.__penColour = turtle.pencolor(
            colour1)  # Breaks walls between cells by drawing the colour of the background over it

    def right(self):  # Function to draw a line between the current cell and the cell to its right
        turtle.up()
        turtle.goto(self._x + self._cellWidth, self._y)
        turtle.down()
        turtle.goto(self._x + self._cellWidth, self._y + self._cellWidth)
        turtle.goto(self._x + self._cellWidth, self._y)
        x, y = self._x + self._cellWidth, self._y

        btmX, btmY = self._x + self._cellWidth, self._y
        tpX, tpY = self._x + self._cellWidth, self._y + self._cellWidth
        brknWalls.append([btmX, btmY, tpX, tpY])  # Appends characteristics of the broken wall to uniquely identify it
        return x, y

    def left(self):  # Function to draw a line between the current cell and the cell to its left
        turtle.up()
        turtle.goto(self._x, self._y)
        turtle.down()
        turtle.goto(self._x, self._y + self._cellWidth)
        turtle.goto(self._x, self._y)
        x, y = self._x - self._cellWidth, self._y

        btmX, btmY = self._x, self._y
        tpX, tpY = self._x, self._y + self._cellWidth
        brknWalls.append([btmX, btmY, tpX, tpY])
        return x, y

    def above(self):  # Function to draw a line between the current cell and the cell above it
        turtle.up()
        turtle.goto(self._x, self._y + self._cellWidth)
        turtle.down()
        turtle.goto(self._x + self._cellWidth, self._y + self._cellWidth)
        turtle.goto(self._x, self._y + self._cellWidth)
        x, y = self._x, self._y + self._cellWidth

        lftX, lftY = self._x, self._y + self._cellWidth
        rgtX, rgtY = self._x + self._cellWidth, self._y + self._cellWidth
        brknWalls.append([lftX, lftY, rgtX, rgtY])
        return x, y

    def below(self):  # Function to draw a line between the current cell and the cell below it
        turtle.up()
        turtle.goto(self._x, self._y)
        turtle.down()
        turtle.goto(self._x + self._cellWidth, self._y)
        turtle.goto(self._x, self._y)
        x, y = self._x, self._y - self._cellWidth

        lftX, lftY = self._x, self._y
        rgtX, rgtY = self._x + self._cellWidth, self._y
        brknWalls.append([lftX, lftY, rgtX, rgtY])
        return x, y

    def starterWall(self):  # Function to draw opening of the maze
        starterEndingRoutine(-300, -300)

    def endingWall(self):  # Function to draw the closing of the maze
        x, y = gridPoints.pop()
        starterEndingRoutine(x, y + self._cellWidth)


# Functions
def starterEndingRoutine(x, y):  # This function is called to draw the opening and the closing of the maze
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.goto(x + cellDimensions, y)


def jumper():  # Part of the backjumping algorithm; it jumps to different cells (randomly) that have been visited
    randomPoint = randint(0, len(visitedCells) - 1)
    turtle.up()
    x, y = visitedCells[randomPoint]  # x,y is set to a random point that has already been visited
    turtle.goto(x, y)
    turtle.down()
    return x, y


def backJumper(x, y):
    for i in range(10):
        # The four conditions that determine whether the program needs to backjump or not
        condition1 = [x + cellDimensions, y] in visitedCells and [x + cellDimensions, y] in gridPoints
        condition2 = [x - cellDimensions, y] in visitedCells and [x - cellDimensions, y] in gridPoints
        condition3 = [x, y + cellDimensions] in visitedCells and [x, y + cellDimensions] in gridPoints
        condition4 = [x, y - cellDimensions] in visitedCells and [x, y - cellDimensions] in gridPoints
        if (x, y) == (-300, -300) and condition3 and condition1:
            x, y = jumper()
        # Checks X's
        elif x == -300 and condition1 and condition3 and condition4:
            x, y = jumper()
        elif x == -300 + (cellDimensions * (gridDimensions - 1)) and condition2 and condition3:
            x, y = jumper()
        elif x == -300 + (cellDimensions * (gridDimensions - 1)) and condition2 and condition3 and condition4:
            x, y = jumper()
        # Checks Y's
        elif y == -300 and condition1 and condition2 and condition3:
            x, y = jumper()
        elif y == -300 and condition1 and condition4:
            x, y = jumper()
        elif y == -300 + (cellDimensions * (gridDimensions - 1)) and condition1 and condition4:
            x, y = jumper()
        # Checks all 4 conditions
        elif condition1 and condition2 and condition3 and condition4:
            x, y = jumper()
    return x, y


def createPath(x, y):  # Function creates a random path through the maze from start to finish
    x, y = -300, -300
    lastPointX, lastPointY = gridPoints[-1]  # Finds the last point (the point that the ending wall belongs to)

    while turtle.position() != (lastPointX + cellDimensions, lastPointY):
        visitedCells.append([x, y])  # Creates the 2D array of visited cells
        direction = randint(0, 3)  # Decides in which direction the next wall will be broken
        if turtle.position() == (lastPointX, lastPointY):  # Ensures the correct wall is broken to finish off the path
            x, y = BreakWall(x, y, cellDimensions, gridDimensions, colour1).right()
        elif turtle.position() == (lastPointX + cellDimensions,
                                   lastPointY - cellDimensions):  # Ensures the correct wall is broken to finish off the path
            x, y = BreakWall(x, y, cellDimensions, gridDimensions, colour1).above()

        elif direction == 0:
            if [x + cellDimensions, y] not in visitedCells and [x + cellDimensions, y] in gridPoints:
                x, y = BreakWall(x, y, cellDimensions, gridDimensions, colour1).right()
            elif [x + cellDimensions, y] in visitedCells and [x + cellDimensions, y] in gridPoints:
                x, y = backJumper(x,
                                  y)  # Calls the backjumper function if the next cell that has been chosen has already been visited
            elif [x + cellDimensions, y] not in gridPoints:
                direction = randint(0, 3)

        elif direction == 1:
            if [x - cellDimensions, y] not in visitedCells and [x - cellDimensions,
                                                                y] in gridPoints:  # Checks that the chosen cell hasn't already been visited before breaking the wall
                x, y = BreakWall(x, y, cellDimensions, gridDimensions, colour1).left()
            elif [x - cellDimensions, y] in visitedCells and [x - cellDimensions, y] in gridPoints:
                x, y = backJumper(x, y)
            elif x <= -300:
                direction = randint(0, 3)
            elif [x - cellDimensions, y] not in gridPoints:
                direction = randint(0, 3)

        elif direction == 2:
            if [x, y + cellDimensions] not in visitedCells and [x, y + cellDimensions] in gridPoints:
                x, y = BreakWall(x, y, cellDimensions, gridDimensions, colour1).above()
            elif [x, y + cellDimensions] in visitedCells and [x, y + cellDimensions] in gridPoints:
                x, y = backJumper(x, y)
            elif [x, y + cellDimensions] not in gridPoints:
                direction = randint(0, 3)

        elif direction == 3:
            # direction=randint(0,3)
            if [x, y - cellDimensions] not in visitedCells and [x, y - cellDimensions] in gridPoints:
                x, y = BreakWall(x, y, cellDimensions, gridDimensions, colour1).below()
            elif [x, y - cellDimensions] in visitedCells and [x, y - cellDimensions] in gridPoints:
                x, y = backJumper(x, y)
            elif [x, y - cellDimensions] not in gridPoints:
                direction = randint(0, 3)


def completeMaze():  # Function to complete the maze after the path has fully been drawn
    for [x, y] in gridPoints:
        if [x, y] not in visitedCells:
            if [x, y] == [-300 + ((gridDimensions - 1) * cellDimensions), -300]:
                x, y = BreakWall(x, y, cellDimensions, gridDimensions, colour1).left()
            if [x, y] == [-300, -300 + ((gridDimensions - 1) * cellDimensions)]:
                x, y = BreakWall(x, y, cellDimensions, gridDimensions, colour1).right()
            direction = randint(0, 1)
            if direction == 0 and x != -300:
                x, y = BreakWall(x, y, cellDimensions, gridDimensions, colour1).left()
            elif direction == 1 and y != -300:
                x, y = BreakWall(x, y, cellDimensions, gridDimensions, colour1).below()
            elif direction == 0 and x == -300:
                x, y = BreakWall(x, y, cellDimensions, gridDimensions, colour1).above()
            elif direction == 1 and y == -300:
                x, y = BreakWall(x, y, cellDimensions, gridDimensions, colour1).right()
            else:
                x, y = gridPoints[randint(0, len(gridPoints) - 1)]
        else:
            x, y = gridPoints[randint(0, len(gridPoints) - 1)]


def levelInfo(level):
    # 2D array = Levels: [length/width of cell, number of cells in each row/column]d
    levelDims = [[200, 3], [150, 4], [120, 5], [100, 6], [90, 7], [70, 8], [70, 9], [60, 10], [56, 11], [50, 12],
                 [46, 13], [44, 14], [40, 15], [38, 16], [36, 17], [30, 20], [10, 60]]
    levelDimensions, gridDimensions = levelDims[level][0], levelDims[level][1]
    return levelDimensions, gridDimensions


def createGrid(x, y):  # Loops the create row function to create the final grid
    for i in range(0, gridDimensions):
        Grid(x, y, cellDimensions, gridDimensions).createRow()
        y += cellDimensions
        turtle.up()
        turtle.goto(x, y)
        turtle.down()


# Main Body
gridPoints, visitedCells = [], []  # Keeps track of all points on the grid, will turn into a 2D array
brknWalls = []  # Stores all the broken walls - this is later used for collisions for the player
x, y = -300, -300  # The beginning co-ordinates; the level is controlled by thie last variable

# Sets the screen up

from OptionsPage import colour1, colour2, colour3

background, pen = colour1, colour2
windowMaze.bgcolor(background)
turtle.pencolor(pen)

from LevelsPage import level

if __name__ == "CreateMaze":
    cellDimensions, gridDimensions = levelInfo(
        level)  # Setting the cell dimension equal to the appropriate length from the 2D array levelDims
    createGrid(x, y)
    BreakWall(x, y, cellDimensions, gridDimensions, colour1).starterWall()
    BreakWall(x, y, cellDimensions, gridDimensions, colour1).endingWall()
    createPath(x, y)
    completeMaze()
    input("Hit Enter")
    windowMaze.setup(400, 700)
    from MessagePage import *

windowMaze.mainloop()
