# Robert Bayer
# Challenge Assignment 1
# Rolls 600 dice and makes a visualization of the data via a bar graph

import random
import numpy as np
from matplotlib import pyplot as pt


def diceroll():
    return random.randint(2, 12)


def makedata(rolls):
    dataset = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for amount in range(rolls):
        dataset[diceroll()] += 1
    return dataset


def main():
    rolls = ""
    while not rolls.isdigit():
        rolls = input("How many rolls would you like to conduct? ")
    rolls = int(rolls)
    bigdata = makedata(rolls)

    #making the graph
    height = []
    bars = list(bigdata)
    print(bars)
    pt.xlabel("Rolls Amount")
    pt.ylabel("Amount of Rolls")
    pt.title("Graphing the Rolls\nof Two Die")
    y_pos = np.arange(len(bigdata))
    for data in bigdata:
        height.append(bigdata[data])
    for i in range(len(bars)):
        pt.text(x=bars[i]-2.19, y=height[i]+3, s=height[i], size=8)
        pt.text(x=bars[i]-2.19, y=height[i]+1.25, s=round((height[i]/rolls)*100, 2), size=8)
    pt.bar(y_pos, height)
    pt.xticks(y_pos, bars)

    pt.show()





main()
