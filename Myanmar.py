from turtle import *

getscreen().bgcolor('white')
color('white')
penup()
goto(-200,200)
pendown()


fillcolor('yellow')
begin_fill()
forward(300)
left(90)
forward(100)
left(90)
forward(300)
left(90)
forward(100)
end_fill()

fillcolor('green')
begin_fill()
forward(100)
left(90)
forward(300)
left(90)
forward(100)
left(90)
forward(300)
end_fill()

left(90)

fillcolor('red')
begin_fill()
forward(200)
left(90)
forward(300)
left(90)
forward(100)
left(90)
forward(300)
end_fill()


fillcolor('white')
penup()
goto(50,170)
left(35)
pendown()
begin_fill()
for i in range(5):
    forward(200)
    left(216)
end_fill()
done()