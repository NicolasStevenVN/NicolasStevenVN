from turtle import *

right(90)

pos = [(-40,0), (40,0)]
for x,y in pos:
    up()
    goto(x,y)
    down()

    fillcolor('red')
    begin_fill()
    for i in range(2):
        forward(200)
        left(90)
        forward(40)
        left(90)
    end_fill()

up()
goto(-40,0)
down()

fillcolor('red')
begin_fill()

right(0)
forward(90)
right(-90)
forward(120)
right(90)
forward(20)
right(90)
forward(120)
right(90)
forward(20)

end_fill()

done()