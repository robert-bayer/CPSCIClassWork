#Robert Bayer
#Module 6 Class Activity 3

#1
#   10

#2
#   HelloHello

#3
import random
def StringThing(myString):
    count = 0
    x = len(myString)
    y = random.randint(0, x)
    print(myString[y])
    for i in range(0, x):
        if myString[i] == "a":
            count += 1
    print(count)

the_string = input("Enter a string: ")

StringThing(the_string)
