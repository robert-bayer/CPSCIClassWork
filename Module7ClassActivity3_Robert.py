#Module 7 Class Activity 3
#Robert Bayer

#1
import math

print("Degrees" + "\t" + "Radians" + "\t" + "\t" + "sin()" + "\t" + "\t" + "cos()")
for degrees in range(0,361, 30):
    rads = math.radians(degrees)
    sinValue = math.sin(rads)
    cosValue = math.cos(rads)
    print(f'{degrees}',f'{rads:.3f}',f'{sinValue:.3f}',f'{cosValue:.3f}', sep='\t' + '\t')

#2
MAX_NUM = 15
for i in range(1, MAX_NUM + 1):
    for j in range(1, MAX_NUM + 1):
        print(i*j, end= '\t')
    print()
#It displays a "Times Table"

#3
BASE = 10

for k in range( BASE ):
    for h in range( BASE ):
        print(k, h, sep="")
#It counts up by crafting one number at a time and appending one onto the other