from turtle import *

def polygon(length, sides):
    for i in range(sides):
        forward(length)
        left(360/sides)
      
polygon(100, 8)
penup()
backward(200)
pendown()
polygon(40, 12)
penup()
left(90)
backward(100)
right(90)
pendown()
polygon(50, 6)

