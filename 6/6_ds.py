from turtle import *

screensize(5000, 5000)
tracer(1)
left(90)
r = 20

for x in range(777):
    forward(25 * r)
    left(90)
    forward(34 * r)
    left(90)

up()

forward(12 * r)
left(90)
forward(17 * r)
right(90)

down()

for x in range(1996):
    forward(25 * r)
    left(90)
    forward(17 * r)
    left(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3)

#1054
done()