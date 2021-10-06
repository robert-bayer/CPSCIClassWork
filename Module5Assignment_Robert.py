#Name: Module 5 Assignment
#Author: Robert Bayer
#Description: Doing the work you want

#   1. Return multiple values and calling the function with brackets with the desired value
#   2.
def prism_volume(height, width, length):
    volume = height * width * length
    return volume
height = int(input("Enter the height of the prism: "))
width = int(input("Enter the width of the prism: "))
length = int(input("Enter that length of the prism: "))

print(prism_volume(height,width,length))
#   3. It takes a variable or answer calculated or given within the function and moves it up a level into the function
#      or program it is in
#   4.
def sphereVolume(radius):
    volume = 4 / 3 * 3.14 * radius ** 3
    return volume

for radius in range(1,5):
    print("The volume of a sphere with a radius of", radius, "is", sphereVolume(radius))
#   5.
def sumTo(n):
    iterator = 1
    number = n
    total = 0
    while iterator <= number:
        total += iterator
        iterator += 1
    return total
n = int(input("Enter a number: "))
print(sumTo(n))

#   6.

import turtle

def drawStar(turtle, n):
    for i in range(1,n+1):
        turtle.fd(100)
        turtle.right(180-(180/n))

def main():
    wn = turtle.Screen()
    crush = turtle.Turtle()
    for i in range(3, 11+1, 2):
        drawStar(crush, i)
        crush.fd(100)
    wn.exitonclick()

if __name__ == "__main__":
    main()