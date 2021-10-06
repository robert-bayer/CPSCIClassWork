#Name: Clock Tower Image
#Author: Robert Bayer
#Date: 8/29/2019
#Decription: Draws a picture of the CSU Clock Tower

import turtle

wn = turtle.Screen()
csu = turtle.Turtle()

#initial parameters
csu.speed(10)
csu.color("MidnightBlue")

#setting up the brush
csu.penup()
csu.goto(100,100)
csu.pendown()
csu.right(90)
csu.begin_fill()

#Beginning of body
csu.forward(100)
csu.right(85)

#Curvy bit
csu.circle(20,50)
csu.circle(5,100)
csu.circle(-5,100)
csu.circle(-20,30)
csu.forward(130)

#Other side of body
csu.setheading(90)
csu.forward(170)

#Begin the top
csu.right(45)
csu.circle(-85,30)

#clock tower
csu.setheading(90)
csu.forward(20)
csu.left(90)
csu.forward(5)
csu.right(95)
csu.forward(40)
csu.setheading(0)
csu.forward(20)
csu.left(60)
csu.forward(20)
csu.setheading(0)
csu.forward(5)
csu.right(60)
csu.forward(50)
csu.right(180)
csu.right(10)
csu.forward(29)
csu.setheading(0)
csu.forward(20)
csu.right(85)
csu.forward(40)
csu.setheading(180)
csu.forward(10)
csu.left(90)
csu.forward(50)
csu.left(45)
csu.forward(5)
csu.setheading(90)
csu.forward(33)
csu.setheading(0)
csu.circle(-90,21)

#fill it
csu.end_fill()

wn.exitonclick()