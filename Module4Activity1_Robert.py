import random

MAX_NUM = 2**32
humanGeneratedNumber = int(input("Please enter a number between 0 and " + str(MAX_NUM) + ": "))
print("If you need a real number between 0.0 and 1.0 use", random.random())
print("If you need an int between 0 and 100 use", random.randrange(0,101))