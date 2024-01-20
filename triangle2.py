from turtle import *

def drawtriangle():
    pencolor('black')
    begin_fill()
    for i in range(3):
        forward(80)
        left(120)
    end_fill()

penup()
goto(-250,0)
pendown()
bgcolor('violet')
fillcolor('yellow')
pensize(5)

for i in range(5):
    drawtriangle()
    penup()
    forward(100)
    pendown()