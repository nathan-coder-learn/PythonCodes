from turtle import *
from random import *

def drawtriangle():
    begin_fill()
    for i in range(3):
        forward(80)
        left(120)
    end_fill()

def triangle_row():
    for i in range(5):
        drawtriangle()
        penup()
        forward(100)
        pendown()
    penup()
    backward(250)

coloor = ["firebrick", "wheat", "snow", "khaki", "navy", "burlywood", "bisque", "thistle"]
pencolor('black')
penup()
goto(-250,160)
pendown()
bgcolor(choice(coloor))
pensize(5)

for i in range(4):
    fillcolor(coloor[i])
    triangle_row()
    left(90)
    backward(125)
    right(90)
    backward(250)
    pendown()