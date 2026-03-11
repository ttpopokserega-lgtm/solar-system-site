import turtle

turtle.shape("turtle")
for y in range(8):
    turtle.forward(100)
    for i in range(8):
        turtle.forward(30)
        turtle.backward(30)
        turtle.right(45)
    turtle.backward(100)
    turtle.right(45)