from turtle import *

screensize(5000, 5000)
tracer(0)
xSize = 20
left(90)

for x in range(2):
    fd(xSize)
    left(270)
    fd(16 * xSize)
    right(90)

up()

bk(4 * xSize)
right(90)
fd(10 * xSize)
left(90)

down()

for x in range(2):
    fd(17 * xSize)
    right(90)
    fd(7 * xSize)
    right(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * xSize, y * xSize)
        dot(3)

done()

#129, правильно