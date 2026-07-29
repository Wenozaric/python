from turtle import *

screensize(5000, 5000)
tracer(0)
k = 20

left(90)

for x in range(2):
    forward(6 * k)
    right(90)
    forward(12 * k)
    right(90)

up()

forward(1 * k)
right(90)
forward(3 * k)
left(90)

down()

for x in range(2):
    forward(77 * k)
    right(90)
    forward(45 * k)
    right(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3)

done()