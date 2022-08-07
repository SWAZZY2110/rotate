#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 19:04:04 2022

@author: priyankadas
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 18:52:34 2022

@author: priyankadas
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Rotate thing")
root.geometry("400x400")
root.configure(bg = "lightblue")

#image
diceimg = Image.open("dice1.4.jpg")
dice = ImageTk.PhotoImage(diceimg)

l3 = Label(root, bg = "gold2", highlightthickness = 5, borderwidth = 2, relief = SOLID)

def show():
    l3["image"] = dice
    
def rotate():
    global diceimg
    global dice
    dice = ImageTk.PhotoImage(diceimg.rotate(45))
    l3["image"] = dice

    
b1 = Button(root, text = "Show Image", command = show)
b2 = Button(root, text = "Rotate Image", command = rotate)
b1.place(relx = 0.50, rely = 0.375,anchor = CENTER)
l3.place(relx = 0.50, rely = 0.500, anchor = CENTER)
b2.place(relx = 0.50, rely = 0.875, anchor = CENTER)

root.mainloop()