from turtle import *
Pen()
bgcolor("black")
colors = ["red", "yellow", "blue", "green", 'cyan', 'white', 'orange', 'purple']
speed(20)
for x in range(400):
    pencolor(colors[x%8])
    #forward(x)
    #circle(x)
    left(91)


done()