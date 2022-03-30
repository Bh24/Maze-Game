##This module allows the user to navigate their way through the maze
from turtle import *
from CreateMaze import *


# RUN THIS MODULE

class Player():
    def __init__(self, shape, color):
        self.trtlState = turtle.up()
        self.shape = turtle.shape(shape)  # the shape of the player
        self.color = turtle.color(colour3)  # the colour of the player
        self.shapeMvmnt = cellDimensions / 2  # Used to position the player

    def getShpMvmnt(self):
        return self.shapeMvmnt

    def start(self):
        lvlSize = [[3, 7], [4, 6], [5, 5], [6, 3.5], [7, 3], [8, 2], [9, 2], [10, 1.5], [11, 1.5], [12, 1.25],
                   [13, 1.25], [14, 1.1], [15, 1.0], [16, 1.0], [17, 0.9], [15, 0.7], [16, 0.01]]
        turtle.shapesize(lvlSize[level][1], lvlSize[level][1], None)
        startPos = -300 + self.shapeMvmnt
        turtle.goto(startPos, startPos)  # Where the player starts
        return startPos

    def up(self):
        x, y = trtlePos()
        if wallA(x, y) is True:  # Checks the wall above has been broken
            turtle.setheading(90)
            turtle.forward(cellDimensions)  # Moves the player
            routeTaken.append([x, y + cellDimensions])

    def down(self):
        x, y = trtlePos()
        if wallB(x, y) is True:
            turtle.setheading(270)  # Changes the direction that the player is facing
            turtle.forward(cellDimensions)
            routeTaken.append([x, y - cellDimensions])

    def left(self):
        x, y = trtlePos()
        if wallL(x, y) is True:  # Checks if the wall to the left has been broken
            turtle.setheading(180)
            turtle.forward(cellDimensions)
            routeTaken.append([x - cellDimensions, y])

    def right(self):
        x, y = trtlePos()
        if wallR(x, y) is True:
            turtle.setheading(0)
            turtle.forward(cellDimensions)
            routeTaken.append([x + cellDimensions, y])


def wallA(x, y):
    '''Checks if the wall above has been broken'''
    aboveWall = [x - shapeMvmnt, y + shapeMvmnt, x + shapeMvmnt, y + shapeMvmnt]
    if aboveWall in brknWalls:
        return True


def wallB(x, y):
    '''Checks if the wall below has been broken'''
    belowWall = [x - shapeMvmnt, y - shapeMvmnt, x + shapeMvmnt, y - shapeMvmnt]
    if belowWall in brknWalls:
        return True


def wallL(x, y):
    '''Checks if the wall to the left has been broken'''
    leftWall = [x - shapeMvmnt, y - shapeMvmnt, x - shapeMvmnt, y + shapeMvmnt]
    if leftWall in brknWalls:
        return True


def wallR(x, y):
    '''Checks if the wall to the right has been broken'''
    rightWall = [x + shapeMvmnt, y - shapeMvmnt, x + shapeMvmnt, y + shapeMvmnt]
    if rightWall in brknWalls:
        return True


def trtlePos():
    # Gets the position of the turtle
    x, y = turtle.position()
    x, y = round(x), round(y)
    return x, y


def giveUp():
    trtlePos() == endPos, endPos
    deactivateKeys()


def activateKeys():
    onkey(Player(shape, colour).up, "Up")
    onkey(Player(shape, colour).down, "Down")
    onkey(Player(shape, colour).left, "Left")
    onkey(Player(shape, colour).right, "Right")
    listen()  # Listens for user's arrows input


def deactivateKeys():
    onkey(None, "Up")
    onkey(None, "Down")
    onkey(None, "Left")
    onkey(None, "Right")
    listen()


shape, colour = "square", "red"

cellDimensions, gridDimensions = levelInfo(level)

shapeMvmnt = Player(shape, colour).getShpMvmnt()

startPos = Player(shape, colour).start()  # Starts the player
routeTaken = [[startPos, startPos]]

endPos = round(startPos + cellDimensions * (gridDimensions - 1))
while trtlePos() != (endPos, endPos):
    activateKeys()
deactivateKeys()
windowMaze.setup(700, 700)
