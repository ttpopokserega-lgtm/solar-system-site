import turtle
import random

turtle. shape( 'turtle')
turtle.width(3)

for i in range(12):
    turtle.right(30)
    color=random.choice([ 'blue', 'red', 'yellow', 'green', 'gray', 'brown', 'purple'])
    turtle. color(color)
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
