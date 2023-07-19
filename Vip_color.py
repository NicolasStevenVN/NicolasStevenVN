from turtle import *
import colorsys
bgcolor('black')
speed(200)

n = 36
h = 0

for i in range(460):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h += 1/n
    color(c)
    left(145)

    for j in range(5):
        forward(300)
        left(150)

done()