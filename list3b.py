from random import *
from turtle import *

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
pensize(5)
pendown()
x = choice(coloor)
bgcolor(x)
coloor.remove(x)

for i in range(4):
    x = choice(coloor)
    fillcolor(x)
    coloor.remove(x)
    triangle_row()
    left(90)
    backward(125)
    right(90)
    backward(250)
    pendown()