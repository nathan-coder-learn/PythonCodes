from turtle import *

def drawtriangle():
    pencolor('black')
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

penup()
goto(-250,200)
pendown()
bgcolor('violet')
fillcolor('yellow')
pensize(5)

for i in range(4):
    triangle_row()
    left(90)
    penup()
    backward(125)
    right(90)
    backward(250)
    pendown()