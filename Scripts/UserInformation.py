from tkinter import *
from datetime import *

def appendData(gameName, password,birthday):
    '''Adds the new data to the file'''
    gameName=gameName.get()
    password=password.get()
    birthday=birthday.get()
    File(gameName,password,birthday).addData()

def getData(gameName, password,birthday):
    '''Gets the values of the information that the user entered'''
    gameName=gameName.get()
    password=password.get()
    birthday=birthday.get()
    if File(gameName,password,birthday).checkForData() == True: #If the data entered is valid, it will retrieve all of the user's data
        File(gameName,password,birthday).getRecommendedLevel()
        File(gameName,password,birthday).getScore()   
    else:
        errorMessage=Tk() #Creates a new window for an error message
        errorMessage.geometry("400x200")
        errorMessage.config(bg="Gray85")
        errorLabel=Label(errorMessage,text="THE DETAILS YOU ENTERED WASN'T FOUND",font=100)
        errorLabel.pack()
        errorBtn=Button(errorMessage,text="RETRY",font=100,command=lambda:errorMessage.destroy())
        errorBtn.pack()

def enterData():
    '''Allows the user to enter their data'''
    global gameName,password,birthday
    gNLabel=Label(root,text="ENTER YOUR GAME NAME",bg="Gray85",font=100)
    gNLabel.pack()
    gameName=Entry(root)
    gameName.pack()
    
    pswrd=Label(root,text="ENTER YOUR PASSWORD", bg="Gray85",font=100)
    pswrd.pack()
    password=Entry(root)
    password.pack()

    dateOB=Label(root,text="ENTER YOUR DATE OF BIRTH", bg="Gray85",font=100)
    dateOB.pack()
    birthday=Entry(root)
    birthday.pack()

    gameName,password,birthday=File(gameName,password,birthday).getMainInfo()

    login=Button(root,text="LOGIN",bg="Gray85",command=lambda:getData(gameName,password,birthday))
    login.pack()

    submit=Button(root,text="ADD INFO",bg="Gray85",command=lambda:appendData(gameName,password,birthday))
    submit.pack()

def calcRL(birthYear):
    '''Calculates the recommended level for the user'''
    birthYear=birthYear.split("/")
    age=date.today().year-int(birthYear[2])#Calculates the users' age
    if age>=4 and age<=7 or age>=55 and age<=60:
        rl=2
    elif age>=8 and age<=11:
        rl=5
    elif age>=12 and age<=15:
        rl=9
    elif age>=16 and age<=24:
        rl=12
    elif age>=25 and age<=35:
        rl=10
    elif age>=36 and age<=45:
        rl=7
    elif age>=45 and age<=55:
        rl=4
    elif age>60:
        rl=1
    return rl

class File:
    def __init__(self,gN,pswrd,dOB):
        self.gameName=gN
        self.password=pswrd
        self.dateOfBirth=dOB
        self.rl=calcRL(self.dateOfBirth)

    def getMainInfo(self):
        return self.gameName,self.password,self.dateOfBirth
    
    def checkForData(self):
        '''Checks the entered data to see if it's already on the file'''
        with open("UserData.txt","r") as userFile:
            for eachLine in userFile:
                lines=eachLine.split(",")
                if lines[0]==self.gameName and lines[1]==self.password and lines[2]==self.dateOfBirth:
                    return True
 
    def addData(self,score):
        '''Adds the user's data to the text file'''
        with open("UserData.txt","a") as userFile:
            try:
                print(self.gameName,self.password,self.dateOfBirth,self.rl,score,file=userFile,sep=",")
            except NameError:
                score=0
                print(self.gameName,self.password,self.dateOfBirth,self.rl,score,file=userFile,sep=",")

    def getRecommendedLevel(self):
        '''Retrieves the recommended level for the user'''
        with open("UserData.txt","r") as userFile:
            for eachLine in userFile:
                lines=eachLine.split(",")
                if lines[0] == self.gameName and lines[1] == self.password:
                    return lines[3]
            
    def getScore(self):
        '''Retrieves the current score of the user'''
        with open("UserData.txt","r") as userFile:
            for eachLine in userFile:
                lines=eachLine.split(",")
                if lines[0] == self.gameName and lines[1] == self.password:
                    return lines[4]

    def addScore(self,score):
        '''Adds points to the users' score'''
        with open("UserData.txt","r+") as userFile:
            fileContents=[]
            for eachLine in userFile:
                lines=eachLine.split(",")
                fileContents.append(lines)#Will create a 2D array of all the records in the text file
                if lines[0]==self.gameName and lines[1] == self.password:
                    #Rewrites the new score on the list
                    lines[4]=str(int(lines[4])+score)+"\n"

        with open ("UserData.txt","w") as userFile:
            #Rewrites the data file using the new score
            for eachElement in fileContents:
                eachElement[4]=eachElement[4].strip("\n")
                File(eachElement[0],eachElement[1],eachElement[2]).addData(eachElement[4])


def addTemporary(gameName,password,dateOfBirth):
    '''Adds data to another file for use later on in the game'''
    with open ("TemporaryFile.txt","w") as tempFile:
        print(gameName, password, dateOfBirth, file=tempFile,sep=",")

def readTemporary():
    with open("TemporaryFile.txt","r") as tempFile:
        lineContents=[]
        for line in tempFile:
            infoSep=line.split(",")
            for i in infoSep:
                lineContents.append(i)
            gameName,password,dateOfBirth=lineContents[0],lineContents[1],lineContents[2]
        return gameName,password,dateOfBirth

