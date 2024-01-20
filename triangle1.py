from turtle import *

def drawtriangle():
    begin_fill()
    for i in range(3):
        forward(80)
        left(120)
    end_fill()

bgcolor('violet')
pencolor('black')
fillcolor('yellow')
pensize(5)

drawtriangle()
