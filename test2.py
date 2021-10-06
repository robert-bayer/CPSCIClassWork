import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles

crush = turtle.Turtle()   # Create a turtle, assign to crush (from Finding Nemo)

vertSideLen=45            # length of vertical sides
horSideLen=100            # length of horizontal sides

crush.right(90)
crush.forward(vertSideLen/2)
crush.left(180)           # Turn around
crush.forward(vertSideLen)

wn.exitonclick()