#Name: Lab 11
#Author: Robert Bayer
#Description: Doing what the lab is telling me to do.

#import needed modules
import math

#Adding two numbers
def add(x, y):
    answer = x + y
    return answer

#Subtraction two numbers
def sub(x, y):
    answer = x - y
    return answer

#Multiply the numbers
def mult(x, y):
    answer = x * y
    return answer

#Raise the first number to the second number
def exp(x, y):
    answer = x ** y
    return answer

#Finding the square root of the two numbers
def sqrt(x, y):
    return math.sqrt(x) + math.sqrt(y)


#Asks for numbers
x = int(input("Enter the first number (not a zero): "))
y = int(input("Enter the second number (not a zero): "))

#Tests to see if either number is zero and asks to redefine if one is.
while x == 0:
    x = int(input("""Not a valid entry.
Enter the first number (not a zero): """))
while y == 0:
    y = int(input("""Not a valid entry.
Enter the second number (not a zero): """))

#Execute the functions and display the results
print(add(x,y))
print(sub(x,y))
print(mult(x,y))
print(exp(x,y))
print(sqrt(x,y))