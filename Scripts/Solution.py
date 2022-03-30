##This module will find the route through the maze
from turtle import *
from Player import *

def neighbourCheck(x,y,visitedSet):
    '''Checks the number of neighbours that the cell has'''
    freeCells=[] #List of unvisited cells, uniqe to the current cell that is being checked - makes us of a stack data structure
    visitedSet.append([x,y])
    if wallA(x,y) is True: #wall A is a function from the player module
        if [x,y+cellDimensions] not in visitedSet:
            freeCells.append([x,y+cellDimensions])
    if wallB(x,y) is True: #Checks if the wall below is broken
        if [x,y-cellDimensions] not in visitedSet: #if broken, and the cell hasn't been visited during the solution
            freeCells.append([x,y-cellDimensions])
    if wallR(x,y) is True:
        if [x+cellDimensions,y] not in visitedSet:
            freeCells.append([x+cellDimensions,y])
    if wallL(x,y) is True:
        if [x-cellDimensions,y] not in visitedSet:
            freeCells.append([x-cellDimensions,y])
    return freeCells

def delCoOrds(path):
    '''Deletes every element up until it finds one that has been visited once but still has unvisited neighbours'''
    pos=-1
    while len(path[pos])!=3:
        pos-=1
    coOrd=path[pos]
    
    for i in range(0,pos,-1):
        del(path[-1])
    
    return path
    
def findPath():
    '''Finds the path through the maze'''
    path=[[startPos,startPos]]
    stack=[]
    x,y=startPos,startPos
    turtle.goto(x,y)

    while trtlePos()!=(endPos,endPos):
        freeCells=neighbourCheck(x,y,visitedSet)
        
        if len(freeCells)==1:
            x,y=freeCells.pop()
            path.append([x,y])
            turtle.goto(x,y)

        elif len(freeCells)>1:
            x,y=freeCells.pop(0)
            for i in range(len(freeCells)):
                path.append([x,y,0])
            for i in freeCells:
                stack.append(i)
            turtle.goto(x,y)

        elif len(freeCells)==0:
            path=delCoOrds(path)
            x,y=stack.pop()
            path.append([x,y])
            turtle.goto(x,y)
            
    for i in path:
        if len(i)==3:
            del(i[2])
    return path

def drawPath(finalPath):
    '''Draws the solution'''
    turtle.speed(2)
    turtle.pencolor("Red")
    for i in finalPath: #Draws out the final path
        turtle.goto(i)
        turtle.down()

def pathCompare(finalPath):
    '''Checks if the user took the fastest route'''
    if routeTaken == finalPath:
        return True
    else:
        return False
        
visitedSet=[] #Set of cells that have been visited
finalPath=findPath()
drawPath(finalPath)
pathCompare(finalPath)
from MessagePage import *
