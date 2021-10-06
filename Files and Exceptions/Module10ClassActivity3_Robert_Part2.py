#Robert
#Module 10 Class Activity 3

import turtle
wn = turtle.Screen()
t = turtle.Turtle()

FileObj = open("turtleinstructions.txt", "r")
aline = FileObj.readline()

while aline:
    aline = aline.split()
    if aline[0] == "UP":
        t.penup()
    elif aline[0] == "DOWN":
        t.pendown()
    else:
        x = int(aline[0])
        y = int(aline[1])
        t.goto(x,y)
    aline = FileObj.readline()

FileObj.close()

wn.exitonclick()