from turtle import *

getscreen().bgcolor('orange')
color('yellow')
penup()
goto(-100,100)
pendown()

fillcolor('green')
begin_fill()
forward(300)
left(-90)
forward(100)
left(-90)
forward(300)
left(-90)
forward(100)
end_fill()


fillcolor('red')
begin_fill()
right(-90)
forward(100)
right(-90)
forward(300)
right(-90)
forward(100)
right(-90)
forward(200)
end_fill()


fillcolor('white')
begin_fill()
right(90)
forward(300)
left(-90)
forward(100)
left(-90)
forward(300)
end_fill()


fillcolor('black')
begin_fill()
left(90)
forward(100)
right(-90)
forward(300)
left(90)
forward(100)
end_fill()


done()