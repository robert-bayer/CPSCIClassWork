import random


total = 0

for i in range(100000):
    numberOfTD = random.randrange(3,6)

    total += numberOfTD

print(total)