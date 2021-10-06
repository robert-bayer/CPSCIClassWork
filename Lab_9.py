#Name: Doing the Lab 9 assignment
#Author: Robert Bayer
#Date:8/30/2019
import turtle

wn = turtle.Screen()
c = turtle.Turtle()

wn.bgcolor("skyblue")

c.color("pink","blue")
c.penup()
c.goto(350,0)


#Circle
c.pendown()
c.pensize(10)
c.right(90)
c.begin_fill()
c.circle(-350)
c.end_fill()

c.penup()
c.home()
c.goto(-150, -100)


#Square
c.setheading(0)
c.pendown()
c.color("green","brown")
c.begin_fill()

for i in range(4):
    c.forward(100)
    c.right(90)

c.end_fill()

#Triangle
c.penup()
c.home()
c.goto(-150,100)
c.color("goldenrod","blueviolet")

c.setheading(0)
c.pendown()
c.begin_fill()
for j in range(3):
    c.forward(100)
    c.left(120)
c.end_fill()

#Star
c.penup()
c.home()
c.goto(175,-150)
c.color("Black","White")

c.pendown()
c.setheading(0)
c.begin_fill()
for p in range(5):
    c.right(180)
    c.left(35)
    c.forward(100)

c.end_fill()
#Dodecagon
angle = 150
c.penup()
c.home()
c.goto(100,100)
c.color("red","orange")

c.pendown()
c.setheading(0)
c.begin_fill()
for d in range(12):
    c.forward(30)
    c.left(30)


c.end_fill()
wn.exitonclick()