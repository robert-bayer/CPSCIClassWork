#Pobert Bayer and Charles Charter
#Module 12 Class Activity 4
#Finds number of duplicate words in a sentence ... writes a check amount given in numbers in letters
import random

def dupword(sentence):
    newsentence = sentence.upper()
    sentlist = newsentence.split()
    sentlist.sort()
    word = ""
    for i in sentlist:
        if word == i:
            print(i)
        else:
            word = i

def numtoword(number):
    number = str(number)
    numlst = []
#    numbers = {"numdic": {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "0": ""}, "tensdic": {"1": "Ten", "2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty", "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety", "0": ""}, "teensdic": {"11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen", "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen"}}
    numdic = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "0": ""}
    tensdic = {"1": "Ten", "2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty", "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety", "0": ""}
    teensdic = {"11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen", "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen"}
    dis = number.find(".")
    final = ""
    teens = ""
    hundreds = ""
    tens = ""
    ones = ""
    tencent = ""
    onecent = ""
    if dis == 0:
        numlst.append("Zero")
    elif dis == 1:
        numlst.append(numdic[number[0]])
        numlst.append(f"And {number[dis + 1:]}/100")
        for thing in numlst:
            if final == "":
                final += thing
            else:
                final += " "
                final += thing
    elif dis == 2:
        if number[0:dis] in teensdic:
            numlst.append(teensdic[number[0:dis]])
        else:
            if tensdic[number[0]] == "":
                pass
            else:
                numlst.append(f"{tensdic[number[0]]}")
            if numdic[number[1]] == "":
                pass
            else:
                numlst.append(numdic[number[1]])
    elif dis == 3:
        numlst.append(f"{numdic[number[0]]} Hundred")
        if number[1:dis] in teensdic:
            numlst.append(teensdic[number[1:dis]])
        else:
            if tensdic[number[1]] == "":
                pass
            else:
                numlst.append(f"{tensdic[number[1]]}")
            if numdic[number[2]] == "":
                pass
            else:
                numlst.append(numdic[number[2]])
    elif dis == 4:
        numlst.append(f"{numdic[number[0]]} Thousand")
        numlst.append(f"{numdic[number[1]]} Hundred")
        if number[1:dis] in teensdic:
            numlst.append(teensdic[number[1:dis]])
        else:
            if tensdic[number[2]] == "":
                pass
            else:
                numlst.append(f"{tensdic[number[2]]}")
            if numdic[number[3]] == "":
                pass
            else:
                numlst.append(numdic[number[3]])

    numlst.append(f"And {number[dis + 1:]}/100")
    for thing in numlst:
        if final == "":
            final += thing
        else:
            final += " "
            final += thing
    return final
#    elif dis > 3 and dis < 6:
#        modifier = f"{tens} {ones} Thousand"
#    elif dis == 6:
#        modifier = f"Hundred {tens} {ones} Thousand"
#find the decimal
#find the distance from the decimal to the most sig digit


dupword("The dog jumped over the dog dog and the cat jumped into the cat")
for i in range(25):
    print(numtoword(f"{random.randrange(10000)}.{random.randrange(100)}"))

