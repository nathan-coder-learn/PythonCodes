from turtle import *

speed('fastest')

def drawisely(x, y, q, z):
    goto(x, y)
    pendown()
    goto(q,z)
    penup()

def pattern(interval, size):
    x = size/2
    penup()
    goto(-x, x)
    pendown()
    for i in range(4):
        forward(size)
        right(90)
    for i in range(int(size/interval)+1):
        y = i*interval
        drawisely(-x, x-y, -x+y, -x)
pattern(20, 500) #can be modified
