from turtle import *
from random import *

def drawtriangle():
    fillcolor(choice(coloor))
    begin_fill()
    for i in range(3):
        forward(80)
        left(120)
    end_fill()

coloor = ["firebrick", "wheat", "snow", "khaki", "navy", "burlywood", "bisque", "thistle", "plum", "magenta"]
bgcolor(choice(coloor))
pencolor(choice(coloor))
penup()
goto(-250,0)
pendown()
pensize(5)

for i in range(5):
    drawtriangle()
    penup()
    forward(100)
    pendown()