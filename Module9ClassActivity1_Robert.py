#Robert Bayer
#Module 9 Class Activity 1

def main():
    mylst = ["ice cream", "pie", "water", "fruit", "cake"]
    inx = 0
    total = 0
    dessertsToTry = []
    print(len(mylst))
    print(mylst[2])
    print("pumpkin pie" in mylst)
    mylst = mylst + ["justice"]
    print(mylst)
    h = 0
    classlist = ["Alexander", "Anjali", "Bradley", "Breyonna", "Charles", "Daniel", "Olivia", "Paul", "Robert",
                 "Rohini"]
    for i in classlist:
        print(i)
    print("""
        
        
    """)

    while h < len(classlist):
        print(classlist[h])
        h += 1
    rainfall = [0.09, 0, 0, 0, 0, 0.81, 0, 0, 0, 0, 1.19, 0.08, 0, 0, 0, 0, 0, 0.22, 0.08, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0.77, 0.05, 0]
    for j in rainfall:
        inx = inx + 1
        total = total + j
    average = total / inx
    print(round(average,4))

main()