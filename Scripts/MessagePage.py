from tkinter import *
from UserInformation import *
from Solution import *

gameName,password,dateOfBirth=readTemporary()

root=Tk()
root.title("Message")
root.geometry("600x200")
root.config(bg="Gray85")

lastPos=startPos+(cellDimensions*(gridDimensions-1))#The position that the user should end

def passMsg(score):
    message1=Label(root,text="GREAT JOB\nYOU FOUND THE SHORTEST ROUTE THROUGH THE MAZE", bg="Gray85",font=500)#Displays a message
    message1.pack()
    screMsg1=Label(root,text="SCORE: %s"%score,bg="Gray85",font=500)#Displays the score
    screMsg1.pack()

def complete(score):
    message2=Label(root,text="WELL DONE\n YOU MADE IT TO THE END OF THE MAZE", bg="Gray85",font=500)
    message2.pack()
    screMsg2=Label(root,text="SCORE: %s"%score,bg="Gray85",font=500)
    screMsg2.pack()


score=(File(gameName,password,dateOfBirth).getScore())
if pathCompare(finalPath) == True and (endPos,endPos)==(lastPos,lastPos):
    File(gameName,password,dateOfBirth).addScore(10)
    score=(File(gameName,password,dateOfBirth).getScore())
    passMsg(score)
elif pathCompare(finalPath) == False and (endPos,endPos)==(lastPos,lastPos):
    File(gameName,password,dateOfBirth).addScore(5)
    score=(File(gameName,password,dateOfBirth).getScore())
    complete(score)


    
