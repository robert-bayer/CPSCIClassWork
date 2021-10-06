#Robert Bayer
#Program will take strings and decide the sentiment behind it

def getstrings(analysisObj):
    mylist = analysisObj.readlines()
    for i in range(len(mylist)):
        mylist[i] = mylist[i].replace("\n", "")
    return mylist


def getsentiments(positiveObj, negativeObj):
    positivelist = positiveObj.readlines()
    negativelist = negativeObj.readlines()
    for i in range(len(positivelist)):
        positivelist[i] = positivelist[i].replace("\n", "")
    for i in range(len(negativelist)):
        negativelist[i] = negativelist[i].replace("\n", "")
    return positivelist, negativelist

def getsentpercent(postitive, negative, line):
    poscount = 0
    negcount = 0
    total = 0
    line = line.split()
    for word in line:
        if word in postitive:
            poscount += 1
        elif word in negative:
            negcount += 1
        total += 1
    posper = (poscount / total) * 100
    negper = (negcount / total) * 100
    neuper = ((total - negcount - poscount) / total) * 100
    return posper, negper, neuper


def main():
    positiveObj = open("positive-words.txt", "r")
    negativeObj = open("negative-words.txt", "r")
    analysisObj = open("analyze.txt", "r")
    result = ""
    sentiments = getsentiments(positiveObj, negativeObj)
    positive = sentiments[0]
    negative = sentiments[1]
#    aline = analysisObj.readline()
#    percents = getsentpercent(positive, negative, aline)
#    positivepercent = percents[0]
#    negativepercent = percents[1]
#    print(f"{aline} is {positivepercent}% postive and {negativepercent}% negative.")
    for aline in analysisObj:
        aline.replace("\n", "")
        percents = getsentpercent(positive, negative, aline)
        positivepercent = percents[0]
        negativepercent = percents[1]
        if positivepercent > negativepercent:
            result = "positive"
        elif negativepercent > positivepercent:
            result = "negative"
        else:
            result = "neutral"
        print(aline)
        print(f"This line is {round(positivepercent,4)}% postive and {round(negativepercent,4)}% negative.")
        print(f"This means that the tweet is overall {result}.")
        print("")

main()