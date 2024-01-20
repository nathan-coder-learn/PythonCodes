from random import *
from turtle import *

color = ["gold", "turquoise", "maroon", "khaki", "snow", "thistle", "black", "firebrick"]
fillcolor(choice(color))
bgcolor(choice(color))
pencolor(choice(color))

begin_fill()
for i in range (3):
    forward(80)
    left(120)
end_fill()