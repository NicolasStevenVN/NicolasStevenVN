from turtle import *
from math import * 

getscreen().bgcolor('ivory')
color('cyan')
penup()
goto(-200,200)
pendown()
for i in range(2):
    forward(400)
    left(-90)
    forward(200)
    left(-90)


fillcolor('white')
begin_fill()
forward(400)
left(-90)
forward(100)
left(-90)
forward(200)
right(26.57)
forward(sqrt(50000))
end_fill()


fillcolor('crimson')
begin_fill()
left(-180)
forward(sqrt(50000))
left(26.57)
forward(200)
left(-180)
forward(200)
left(26.57)
forward(sqrt(50000))
end_fill()


fillcolor('navy blue')
begin_fill()
right(-180)
forward(sqrt(50000))
right(26.57)
forward(200)
left(-90)
forward(100)
left(-90)
forward(400)
left(-90)
forward(200)
left(-90)
end_fill()



done()