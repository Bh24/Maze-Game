from tkinter import *


root=Tk() #Sets up a tkinter page
root.title("Choose A Level")
root.geometry("545x560")
root.config(bg="paleVioletRed")

width,height="14","7"

font=300

def command(num): #Sets the level based on which button is pressed
    global levelChosen
    levelChosen=IntVar()
    levelChosen.set(num)
    root.destroy() #Closes the tkinter page and starts creating the maze
    
lvl1=Button(root, text="1", font=font, width=width, height=height,command=lambda: command(0))
lvl1.grid(row=0,column=0) #Gridding the buttons


lvl2=Button(root, text="2", font=font,width=width, height=height,command=lambda: command(1))
lvl2.grid(row=0,column=1)


lvl3=Button(root, text="3",font=font, width=width, height=height,command=lambda: command(2))
lvl3.grid(row=0,column=2)


lvl4=Button(root, text="4",font=font, width=width, height=height,command=lambda: command(3))
lvl4.grid(row=0,column=3)


lvl5=Button(root, text="5",font=font,width=width, height=height,command=lambda: command(4))
lvl5.grid(row=1,column=0)


lvl6=Button(root, text="6",font=font, width=width, height=height,command=lambda: command(5))
lvl6.grid(row=1,column=1)


lvl7=Button(root, text="7", font=font,width=width, height=height,command=lambda: command(6))
lvl7.grid(row=1,column=2)


lvl8=Button(root, text="8",font=font, width=width, height=height,command=lambda: command(7))
lvl8.grid(row=1,column=3)


lvl9=Button(root, text="9", font=font,width=width, height=height,command=lambda: command(8))
lvl9.grid(row=2,column=0)


lvl10=Button(root, text="10", font=font,width=width, height=height,command=lambda: command(9))
lvl10.grid(row=2,column=1)


lvl11=Button(root, text="11",font=font, width=width, height=height,command=lambda: command(10))
lvl11.grid(row=2,column=2)


lvl12=Button(root, text="12",font=font, width=width, height=height,command=lambda: command(11))
lvl12.grid(row=2,column=3)


lvl13=Button(root, text="13", font=font,width=width, height=height,command=lambda: command(12))
lvl13.grid(row=3,column=0)


lvl14=Button(root, text="14", font=font,width=width, height=height,command=lambda: command(13))
lvl14.grid(row=3,column=1)


lvl15=Button(root, text="15", font=font,width=width, height=height,command=lambda: command(14))
lvl15.grid(row=3,column=2)


lvl16=Button(root, text="BONUS LEVEL", font=font,width=width, height=height,command=lambda: command(15))
lvl16.grid(row=3,column=3)

root.mainloop()
level=levelChosen.get()
from CreateMaze import *

