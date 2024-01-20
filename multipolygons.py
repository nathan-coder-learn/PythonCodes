from turtle import *
from random import *

def polygon():
    sides = randint(3,8)
    length = randint(15, 30)
    fillcolor(choice(colors))
    begin_fill()
    for i in range(sides):
        forward(length)
        left(360/sides)
    end_fill()
        
def PolygonRow():
    for i in range(5):
        polygon()
        setheading(0)
        penup()
        forward(80)
        pendown()
 
penup()
goto(-300, 260)
pendown()
colors = ['magenta', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'turquoise', 'orange', 'violet', 'indigo', 'darkorchid', 'cadetblue', 'navy', 'firebrick', 'maroon', 'darkolivegreen', 'tan', 'thistle', 'plum', 'salmon', 'coral', 'ivory']
rows = numinput('RandomHeading', 'How many rows of polygons do you want this program to draw???')
if int(rows) < 1:
    rows = 1
elif int(rows) > 8:
    rows = 8
    
for i in range(int(rows)):
    PolygonRow()
    penup()
    backward(400)
    left(90)
    backward(80)
    pendown()
    right(90)