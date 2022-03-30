from tkinter import *
root=Tk() #Sets up a tkinter page
root.title("Options")
root.geometry("800x400")

bckgrndColour="Gray85"
root.config(bg=bckgrndColour)

def getBgColour(colour):
    global bckgColour
    bckgColour = StringVar()
    bckgColour.set(colour)
    bgPreview=Label(root,bg=colour,height=8)
    bgPreview.grid(row=6,column=2,sticky="NESW",columnspan=5)

def getMazeColour(colour):
    global lneColour
    lneColour = StringVar()
    lneColour.set(colour)
    lnePreview=Label(root,bg=colour,height=8)
    lnePreview.grid(row=6,column=3)

    lnePreview2=Label(root,bg=colour,height=8)
    lnePreview2.grid(row=6,column=5)

def getCharacterColour(colour):
    global chrColour
    chrColour=StringVar()
    chrColour.set(colour)
    chrPreview=Label(root,bg=colour,height=2,width=4)
    chrPreview.grid(row=6,column=4)

def gotoMenu():
    root.destroy()
    
width,height="3","2"

def backgroundColour(width,height):
    bgColour=Label(root,text="Background Colour:",bg=bckgrndColour,font=100)
    bgColour.grid(row=0,column=0,sticky="NESW")

    bg1=Button(root,width=width,height=height,bg="White",command=lambda: getBgColour("White"))
    bg1.grid(row=0,column=1,sticky="NESW") 

    bg2=Button(root,width=width,height=height,bg="Peach Puff", command=lambda:getBgColour("Peach Puff"))
    bg2.grid(row=0,column=2,sticky="NESW")

    bg3=Button(root,width=width,height=height,bg="LightSalmon2",command=lambda:getBgColour("LightSalmon2"))
    bg3.grid(row=0,column=3,sticky="NESW")

    bg4=Button(root,width=width,height=height,bg="PaleVioletRed2",command=lambda:getBgColour("PaleVioletRed2"))
    bg4.grid(row=0,column=4,sticky="NESW")

    bg5=Button(root,width=width,height=height,bg="Coral2",command=lambda:getBgColour("Coral2"))
    bg5.grid(row=0,column=5,sticky="NESW")

    bg6=Button(root,width=width,height=height,bg="Tomato3",command=lambda:getBgColour("Tomato3"))
    bg6.grid(row=0,column=6,sticky="NESW")

    bg7=Button(root,width=width,height=height,bg="Red3",command=lambda:getBgColour("Red3"))
    bg7.grid(row=0,column=7,sticky="NESW")

    bg8=Button(root,width=width,height=height,bg="OrangeRed2",command=lambda:getBgColour("OrangeRed2"))
    bg8.grid(row=0,column=8,sticky="NESW")

    bg9=Button(root,width=width,height=height,bg="DarkOrange2",command=lambda:getBgColour("DarkOrange2"))
    bg9.grid(row=0,column=9,sticky="NESW")

    bg10=Button(root,width=width,height=height,bg="DarkGoldenrod1",command=lambda:getBgColour("DarkGoldenrod1"))
    bg10.grid(row=0,column=10,sticky="NESW")

    bg11=Button(root,width=width,height=height,bg="Yellow2",command=lambda:getBgColour("Yellow2"))
    bg11.grid(row=0,column=11,sticky="NESW")

    bg12=Button(root,width=width,height=height,bg="Spring Green",command=lambda:getBgColour("Spring Green"))
    bg12.grid(row=0,column=12,sticky="NESW")

    bg13=Button(root,width=width,height=height,bg="Green2",command=lambda:getBgColour("Green2"))
    bg13.grid(row=0,column=13,sticky="NESW")

    bg14=Button(root,width=width,height=height,bg="SpringGreen4",command=lambda:getBgColour("SpringGreen4"))
    bg14.grid(row=0,column=14,sticky="NESW")

    bg15=Button(root,width=width,height=height,bg="Cyan4",command=lambda:getBgColour("Cyan4"))
    bg15.grid(row=0,column=15,sticky="NESW")

    bg16=Button(root,width=width,height=height,bg="Medium Turquoise",command=lambda:getBgColour("Medium Turquoise"))
    bg16.grid(row=0,column=16,sticky="NESW")

    bg17=Button(root,width=width,height=height,bg="DarkSlateGray1",command=lambda:getBgColour("DarkSlateGray1"))
    bg17.grid(row=0,column=17,sticky="NESW")

    bg18=Button(root,width=width,height=height,bg="LightSteelBlue2",command=lambda:getBgColour("LightSteelBlue2"))
    bg18.grid(row=0,column=18,sticky="NESW")

    bg19=Button(root,width=width,height=height,bg="Violet",command=lambda:getBgColour("Violet"))
    bg19.grid(row=0,column=19,sticky="NESW")

    bg20=Button(root,width=width,height=height,bg="DarkViolet",command=lambda:getBgColour("DarkViolet"))
    bg20.grid(row=0,column=20,sticky="NESW")

    bg21=Button(root,width=width,height=height,bg="Black",command=lambda:getBgColour("Black"))
    bg21.grid(row=0,column=21,sticky="NESW")

    line2=Label(root,bg=bckgrndColour)
    line2.grid(row=1,column=0)

def charColour(width,height):
    shape=Label(root,text="Character Colour", bg=bckgrndColour, font=150)
    shape.grid(row=4,column=0,sticky="NESW")

    line3=Label(root,bg=bckgrndColour)
    line3.grid(row=3,column=0)

    shp1=Button(root,width=width,height=height,bg="White",command=lambda: getCharacterColour("White"))
    shp1.grid(row=4,column=21,sticky="NESW")

    shp2=Button(root,width=width,height=height,bg="PeachPuff",command=lambda: getCharacterColour("Peach Puff"))
    shp2.grid(row=4,column=20,sticky="NESW")

    shp3=Button(root,width=width,height=height,bg="LightSalmon2",command=lambda: getCharacterColour("LightSalmon2"))
    shp3.grid(row=4,column=19,sticky="NESW")

    shp4=Button(root,width=width,height=height,bg="PaleVioletRed2",command=lambda: getCharacterColour("PaleVioletRed2"))
    shp4.grid(row=4,column=18,sticky="NESW")

    shp5=Button(root,width=width,height=height,bg="Coral2",command=lambda: getCharacterColour("Coral2"))
    shp5.grid(row=4,column=17,sticky="NESW")

    shp6=Button(root,width=width,height=height,bg="Tomato3",command=lambda: getCharacterColour("Tomato3"))
    shp6.grid(row=4,column=16,sticky="NESW")

    shp7=Button(root,width=width,height=height,bg="Red3",command=lambda: getCharacterColour("Red3"))
    shp7.grid(row=4,column=15,sticky="NESW")

    shp8=Button(root,width=width,height=height,bg="OrangeRed2",command=lambda: getCharacterColour("OrangeRed2"))
    shp8.grid(row=4,column=14,sticky="NESW")

    shp9=Button(root,width=width,height=height,bg="DarkOrange2",command=lambda: getCharacterColour("DarkOrange2"))
    shp9.grid(row=4,column=13,sticky="NESW")

    shp10=Button(root,width=width,height=height,bg="DarkGoldenrod1",command=lambda: getCharacterColour("DarkGoldenrod1"))
    shp10.grid(row=4,column=12,sticky="NESW")

    shp11=Button(root,width=width,height=height,bg="Yellow2",command=lambda: getCharacterColour("Yellow2"))
    shp11.grid(row=4,column=11,sticky="NESW")

    shp12=Button(root,width=width,height=height,bg="Spring Green",command=lambda: getCharacterColour("Spring Green"))
    shp12.grid(row=4,column=10,sticky="NESW")

    shp13=Button(root,width=width,height=height,bg="Green2",command=lambda: getCharacterColour("Green2"))
    shp13.grid(row=4,column=9,sticky="NESW")

    shp14=Button(root,width=width,height=height,bg="SpringGreen4",command=lambda: getCharacterColour("SpringGreen4"))
    shp14.grid(row=4,column=8,sticky="NESW")

    shp15=Button(root,width=width,height=height,bg="Cyan4",command=lambda: getCharacterColour("Cyan4"))
    shp15.grid(row=4,column=7,sticky="NESW")

    shp16=Button(root,width=width,height=height,bg="Medium Turquoise",command=lambda: getCharacterColour("Medium Turquoise"))
    shp16.grid(row=4,column=6,sticky="NESW")

    shp17=Button(root,width=width,height=height,bg="DarkSlateGray1",command=lambda: getCharacterColour("DarkSlateGray1"))
    shp17.grid(row=4,column=5,sticky="NESW")

    shp18=Button(root,width=width,height=height,bg="LightSteelBlue2",command=lambda: getCharacterColour("LightSteelBlue2"))
    shp18.grid(row=4,column=4,sticky="NESW")

    shp19=Button(root,width=width,height=height,bg="Violet",command=lambda: getCharacterColour("Violet"))
    shp19.grid(row=4,column=3,sticky="NESW")

    shp20=Button(root,width=width,height=height,bg="Dark Violet",command=lambda: getCharacterColour("DarkViolet"))
    shp20.grid(row=4,column=2,sticky="NESW")

    shp21=Button(root,width=width,height=height,bg="Black",command=lambda: getCharacterColour("Black"))
    shp21.grid(row=4,column=1,sticky="NESW")

def lineColour(width,height):
    mazeColour=Label(root,text="Maze Colour:",bg=bckgrndColour,font=150)
    mazeColour.grid(row=2,column=0,sticky="NESW")

    mz1=Button(root,width=width,height=height,bg="White",command=lambda: getMazeColour("White"))
    mz1.grid(row=2,column=21,sticky="NESW")

    mz2=Button(root,width=width,height=height,bg="PeachPuff",command=lambda: getMazeColour("Peach Puff"))
    mz2.grid(row=2,column=20,sticky="NESW")

    mz3=Button(root,width=width,height=height,bg="LightSalmon2",command=lambda: getMazeColour("LightSalmon2"))
    mz3.grid(row=2,column=19,sticky="NESW")

    mz4=Button(root,width=width,height=height,bg="PaleVioletRed2",command=lambda: getMazeColour("PaleVioletRed2"))
    mz4.grid(row=2,column=18,sticky="NESW")

    mz5=Button(root,width=width,height=height,bg="Coral2",command=lambda: getMazeColour("Coral2"))
    mz5.grid(row=2,column=17,sticky="NESW")

    mz6=Button(root,width=width,height=height,bg="Tomato3",command=lambda: getMazeColour("Tomato3"))
    mz6.grid(row=2,column=16,sticky="NESW")

    mz7=Button(root,width=width,height=height,bg="Red3",command=lambda: getMazeColour("Red3"))
    mz7.grid(row=2,column=15,sticky="NESW")

    mz8=Button(root,width=width,height=height,bg="OrangeRed2",command=lambda: getMazeColour("OrangeRed2"))
    mz8.grid(row=2,column=14,sticky="NESW")

    mz9=Button(root,width=width,height=height,bg="DarkOrange2",command=lambda: getMazeColour("DarkOrange2"))
    mz9.grid(row=2,column=13,sticky="NESW")

    mz10=Button(root,width=width,height=height,bg="DarkGoldenrod1",command=lambda: getMazeColour("DarkGoldenrod1"))
    mz10.grid(row=2,column=12,sticky="NESW")

    mz11=Button(root,width=width,height=height,bg="Yellow2",command=lambda: getMazeColour("Yellow2"))
    mz11.grid(row=2,column=11,sticky="NESW")

    mz12=Button(root,width=width,height=height,bg="Spring Green",command=lambda: getMazeColour("Spring Green"))
    mz12.grid(row=2,column=10,sticky="NESW")

    mz13=Button(root,width=width,height=height,bg="Green2",command=lambda: getMazeColour("Green2"))
    mz13.grid(row=2,column=9,sticky="NESW")

    mz14=Button(root,width=width,height=height,bg="SpringGreen4",command=lambda: getMazeColour("SpringGreen4"))
    mz14.grid(row=2,column=8,sticky="NESW")

    mz15=Button(root,width=width,height=height,bg="Cyan4",command=lambda: getMazeColour("Cyan4"))
    mz15.grid(row=2,column=7,sticky="NESW")

    mz16=Button(root,width=width,height=height,bg="Medium Turquoise",command=lambda: getMazeColour("Medium Turquoise"))
    mz16.grid(row=2,column=6,sticky="NESW")

    mz17=Button(root,width=width,height=height,bg="DarkSlateGray1",command=lambda: getMazeColour("DarkSlateGray1"))
    mz17.grid(row=2,column=5,sticky="NESW")

    mz18=Button(root,width=width,height=height,bg="LightSteelBlue2",command=lambda: getMazeColour("LightSteelBlue2"))
    mz18.grid(row=2,column=4,sticky="NESW")

    mz19=Button(root,width=width,height=height,bg="Violet",command=lambda: getMazeColour("Violet"))
    mz19.grid(row=2,column=3,sticky="NESW")

    mz20=Button(root,width=width,height=height,bg="Dark Violet",command=lambda: getMazeColour("DarkViolet"))
    mz20.grid(row=2,column=2,sticky="NESW")

    mz21=Button(root,width=width,height=height,bg="Black",command=lambda: getMazeColour("Black"))
    mz21.grid(row=2,column=1,sticky="NESW")

    line3=Label(root,bg=bckgrndColour)
    line3.grid(row=5,column=0)

    preview=Label(root,text="Preview:",bg=bckgrndColour,font=150)
    preview.grid(row=6,column=0,sticky="NESW")

    done=Button(root,text="DONE",font="100",command=lambda: gotoMenu())
    done.grid(row=8,column=5,columnspan=10)

#Main Body
if __name__=="OptionsPage":
    backgroundColour(width,height)
    lineColour(width,height)
    charColour(width,height)


root.mainloop()
try:
    colour1=bckgColour.get()
    colour2=lneColour.get()
    colour3=chrColour.get()
except NameError:
    colour1,colour2,colour3="White","Black","Red"

from LevelsPage import *
level=levelChosen.get()
from CreateMaze import *
