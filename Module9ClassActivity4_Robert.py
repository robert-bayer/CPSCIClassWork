#Module 9 Class Activity 4
#Robert Bayer

import random

def leapYear(list1, list2):
    age = []
    index = ""
    for i in list1:
        if i % 4 == 0:
            index = list1.index(i)
            age.append(list2[index])
    return age

def numberofyears(list1):
    mysum = 0
    for i in list1:
        if i >= 100:
            mysum += 1
    return mysum

def randomages():
    ages = []
    for i in range(10):
        number = random.randint(0,110)
        ages.append(number)
    print(ages)
    return ages

def randomyears():
    years = []
    for i in range(10):
        number = random.randint(1850, 2010)
        years.append(number)
    print(years)
    return years


for i in range(100):
    list1 = randomyears()
    list2 = randomages()
    years = leapYear(list1, list2)
    results = numberofyears(years)
    print(results)