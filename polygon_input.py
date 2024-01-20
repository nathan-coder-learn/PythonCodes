from turtle import *

def polygon(sides, length):
    fillcolor(color)
    begin_fill()
    for i in range(sides):
        forward(length)
        left(360/sides)
    end_fill()
        
sides = numinput('Sides', 'How many sides would your polygon have?')
polys_lenght = numinput('Length', 'What is the length of your amazing polygon?')
color = textinput('Color', 'What is da color of your brilliant polygon?')
polygon(int(sides), polys_lenght)