import turtle
from random import *

turtles = []
colors = []
avColors = ['azure', 'beige','magenta', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'turquoise', 'orange', 'violet', 'indigo', 'darkorchid', 'cadetblue', 'navy', 'firebrick', 'maroon', 'darkolivegreen', 'tan', 'thistle', 'plum', 'salmon', 'coral', 'ivory', 'darksalmon', 'wheat', 'khaki']
for i in range(10):
    turtles.append(turtle.Turtle())
    colors.append(choice(avColors))
for i in range(10):
    turtles[i].speed('slowest')
    turtles[i].shape('turtle')
    turtles[i].pencolor(colors[i])
    
for i in range(100):
    for i in range(10):
        turtles[i].setheading(randrange(359))
        turtles[i].forward(randint(1, 100))