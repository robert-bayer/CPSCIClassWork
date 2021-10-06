import turtle

wn = turtle.Screen()
c = turtle.Turtle()

c.penup()

side = 150

c.penup()
c.goto(0,0)
c.setheading(0)
c.forward(side)
c.right(120)
c.pendown()

for s in range(0, -150, -30):

    c.pendown()
    for j in range(6):
        c.forward(side)
        c.right(60)
    side -= 30
    c.penup()
    c.goto(120+s,0)

c.pendown()

for l in range(6):
    c.forward(150)
    c.backward(150)
    c.right(60)

wn.exitonclick()