from turtle import *
from random import *

def polygon(sides, length):
    begin_fill()
    for i in range(sides):
        forward(length)
        left(360/sides)
    end_fill()
    
colours =  ['red', 'navy', 'turquoise', 'azure', 'beige','cadetblue','cobaltgreen', 'darkolivegreen', 'firebrick', 'wheat', 'khaki', 'darksalmon', 'blue','green','orange','turquoise','yellow','indigo','violet','darkorchid']   
sides = numinput("Sides","How many sides would your polygon have?")
length = numinput("Length", "How long is your polygon?")
colour = textinput("Color", "What is the color of your polygon?")

if int(sides) <= 2:
    print('You have an invalid input for the number of sides of your polygon.')
    a = False
elif int(length) <= 0:
    print('Your input for the length of the polygon is an invalid one.')
    a = False
else:
    a = True

if colour == 'random':
    fillcolor(choice(colours))
elif colour in colours:
    fillcolor(colour)
else:
    print('Your input for the color of your polygon is invalid.')
    a = False
    
if a == True:
    polygon(int(sides), length)
else:
    write("Failure to execute polygon_input2 due to invalid inputs. Please try again...")

