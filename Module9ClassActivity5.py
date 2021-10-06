#Module 9 Class Activity 5
#Robert Bayer and Rohini Rewatkar
#Taking a list of 3 lists of words and printing it as a table

mylist = [["English", "boy", "girl", "table", "chair", "apple"], ["Spanish", "chico", "chica", "mesa", "silla", "manazana"], ["French", "garcon", "fillette", "table", "chaise", "pomme"]]

x = 0

for i in mylist:
    for j in i:
        if x < len(j):
            x = len(j)


def makealist(mylist, just):
    l1 = mylist[0]
    l2 = mylist[1]
    l3 = mylist[2]
    str1 = ""
    str2 = ""
    str3 = ""

    for i in range(len(l1)):
        str1 = l1[i]
        str2 = l2[i]
        str3 = l3[i]
        print(str1.ljust(just + 3), str2.center(just + 3), str3.rjust(just + 3))


makealist(mylist, x)