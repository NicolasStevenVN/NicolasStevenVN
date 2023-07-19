from turtle import *
  


Pen()
bgcolor("white")


colors = ["red", "yellow", "blue", "green", 'cyan', 'blue', 'orange', 'purple']
speed(11)



# loop for number of squares
for i in range(60):
    pencolor(colors[i%8])
    # loop for drawing each square
    for j in range(4):
        pencolor(colors[i%8])
        # drawing each side of
        # square of length 100 
        fd(100)
          
        # turning 90 degrees
        # to the right
        rt(90)
          
    # turning 6 degrees for
    # the next square
    rt(6)

done()