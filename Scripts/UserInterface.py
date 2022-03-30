from tkinter import *
from UserInformation import *

dataPage=Tk()
dataPage.title("Enter Data")
dataPage.geometry("300x200")
dataPage.config(bg="Gray85")

def addData(gameName, password,birthday):
    '''Adds the new data to the file'''
    gameName=gameName.get()
    password=password.get()
    birthday=birthday.get()
    addTemporary(gameName,password,birthday)
    File(gameName,password,birthday).addData(0)

    dataPage.destroy() #Destroys the window that allowed the user to enter their data
    displayRecommendedLevel(gameName, password,birthday)

def getData(gameName, password,birthday):
    '''Gets the values of the information that the user entered'''
    gameName=gameName.get()
    password=password.get()
    birthday=birthday.get()
    addTemporary(gameName,password,birthday)
    if File(gameName,password,birthday).checkForData() == True: #If the data entered is valid, it will retrieve all of the user's data
        recommendedLevel=File(gameName,password,birthday).getRecommendedLevel()
        score=File(gameName,password,birthday).getScore()
        dataPage.destroy()
        displayRecommendedLevel(gameName, password,birthday)   
    else:
        errorMessage=Tk() #Creates a new window for an error message
        errorMessage.geometry("400x200")
        errorMessage.config(bg="Gray85")
        errorLabel=Label(errorMessage,text="THE DETAILS YOU ENTERED WASN'T FOUND",font=100)
        errorLabel.pack()
        errorBtn=Button(errorMessage,text="RETRY",font=100,bg="Gray85",command=lambda:errorMessage.destroy())
        errorBtn.pack()
    

def enterData():
    '''Allows the user to enter their data'''
    gNLabel=Label(dataPage,text="ENTER YOUR GAME NAME",bg="Gray85",font=100)
    gNLabel.pack()
    gameName=Entry(dataPage)
    gameName.pack()
    
    pswrd=Label(dataPage,text="ENTER YOUR PASSWORD", bg="Gray85",font=100)
    pswrd.pack()
    password=Entry(dataPage)
    password.pack()

    dateOB=Label(dataPage,text="ENTER YOUR DATE OF BIRTH", bg="Gray85",font=100)
    dateOB.pack()
    birthday=Entry(dataPage)
    birthday.pack()

    login=Button(dataPage,text="LOGIN",bg="Gray85",command=lambda:getData(gameName,password,birthday))
    login.pack()

    submit=Button(dataPage,text="ADD INFO",bg="Gray85",command=lambda:addData(gameName,password,birthday))
    submit.pack()


def displayRecommendedLevel(gameName, password,birthday):
    '''This will display the users' recommended level'''
    rLPage=Tk()
    rLPage.title("Your Recommended Level")
    rLPage.geometry("300x200")
    rLPage.config(bg="Gray85")
    rl=File(gameName,password,birthday).getRecommendedLevel()
    msg=Label(rLPage,text="YOUR RECOMMENDED LEVEL: %s"%rl,bg="Gray85")
    msg.pack()
    play=Button(rLPage,text="PLAY",bg="Gray85",command=lambda:rLPage.destroy())
    play.pack()
                   
    
enterData()
dataPage.mainloop()
from OptionsPage import *
