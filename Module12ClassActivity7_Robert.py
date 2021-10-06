#Module 12 Class Activity 7
#Robert Bayer
import re

#TASK A
InFileObj = open("directory.txt", "r")
OutFileObj = open("phonenumbers.txt", "w")
listthing = InFileObj.readlines()
phonelines =[]
phonenumbers = []
reg = ["\d{10}", "\d{3}-\d{3}-\d{4}"]

for regex in reg:
    regcompile = re.compile(regex)
    for item in listthing:
        phnum = regcompile.search(item)
        if phnum:
            print("I have found a number")
            phonelines.append(item)
for i in range(len(phonelines)):
    phonelines[i] = phonelines[i].replace("\n", "")
phonelines = " ".join(phonelines)
for regex in reg:
    regcompile = re.compile(regex)
    phonenumbers = regcompile.findall(phonelines)
    for nums in phonenumbers:
        OutFileObj.write(nums)
        OutFileObj.write("\n")

InFileObj.close()
OutFileObj.close()

#TASK B
