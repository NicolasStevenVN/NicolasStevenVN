import turtle as t


# getting a Screen to work on
ws=t.Screen()
# setting up turtle color to green
t.color("Green")
# Setting Up width to 2
t.width("2")
# Setting up speed to 2
t.speed(2)
# Loop for making outside square of
# length 300
for i in range(4):
    t.forward(300)
    t.left(90)
# code for inner lines of the square
t.penup()
t.goto(0,100)
t.pendown()
t.forward(300)
t.penup()
t.goto(0,200)
t.pendown()
t.forward(300)
t.penup()
t.goto(100,0)
t.pendown()
t.left(90)
t.forward(300)
t.penup()
t.goto(200,0)
t.pendown()
t.forward(300)
t.done()