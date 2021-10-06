# Robert Bayer and Charles Charter
# Class Activity on Dictionary Task B
# The program will create a tic-tac-toe board for a user to either play against the computer or play against another user
import random


def playernumber():
    choices = ["1", "2"]
    playernum = ""
    while playernum not in choices:
        playernum = input("Would you like to play multiplayer or play against the computer?\n1 for Single Player\n2 for Multi Player\nEnter your choice: ")
    playernum = int(playernum)

    if playernum == 1:
        return True
    elif playernum == 2:
        return False


def getcom(Avbl):
    Avble = Avbl
    comchoice = random.randrange(len(Avble))
    comcol = int(Avble[comchoice][1])
    comrow = Avble[comchoice][0]
    return comcol, comrow


def testwin(row1, row2, row3, winner):
    row1 = row1
    row2 = row2
    row3 = row3
    winner = winner
    winmark = None

    if (row1["Col1"] == row2["Col1"] == row3["Col1"]) and (row1["Col1"] != ""):
        winner = True
        winmark = row1["Col1"]
    elif (row1["Col2"] == row2["Col2"] == row3["Col2"]) and (row1["Col2"] != ""):
        winner = True
        winmark = row1["Col2"]
    elif (row1["Col3"] == row2["Col3"] == row3["Col3"]) and (row1["Col3"] != ""):
        winner = True
        winmark = row1["Col3"]
    elif (row1["Col1"] == row1["Col2"] == row1["Col3"]) and (row1["Col1"] != ""):
        winner = True
        winmark = row1["Col1"]
    elif (row2["Col1"] == row2["Col2"] == row2["Col3"]) and (row2["Col1"] != ""):
        winner = True
        winmark = row2["Col1"]
    elif (row3["Col3"] == row3["Col2"] == row3["Col3"]) and (row3["Col1"] != ""):
        winner = True
        winmark = row3["Col3"]
    elif (row1["Col1"] == row2["Col2"] == row3["Col3"]) and (row1["Col1"] != ""):
        winner = True
        winmark = row1["Col1"]
    elif (row3["Col1"] == row2["Col2"] == row1["Col3"]) and (row3["Col1"] != ""):
        winner = True
        winmark = row3["Col1"]
    else:
        winner = False
        winmark = None
    return winner, winmark


def printboard(row1, row2, row3):

    print(f"""
        |        |
\t{row1["Col1"]}\t|\t{row1["Col2"]}\t |\t{row1["Col3"]}       
________|________|________
        |        |
\t{row2["Col1"]}\t|\t{row2["Col2"]}\t |\t{row2["Col3"]} 
________|________|________
        |        |
\t{row3["Col1"]}\t|\t{row3["Col2"]}\t |\t{row3["Col3"]} 
        |        |    
    """)


def getuser():
    columns = ["Col1", "Col2", "Col3"]
    rows = ["A", "B", "C"]
    col = ["1", "2", "3"]
    userrow = ""
    usercol = ""
    while userrow not in rows:
        userrow = input("What row do you want to pick? ")
    while usercol not in col:
        usercol = input("What column do you want to pick? ")
    usercol = columns[int(usercol) - 1]
    return usercol, userrow


def testtaken(row1, row2, row3):
    row1 = row1
    row2 = row2
    row3 = row3



def main():
    avble = ["A1", "A1", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    winner = False
    winmark = None
    markers = ["X", "O"]
    markerchoice1 = ""
    markerchoice2 = ""
    singleplayer = playernumber()
    getwin = ""
    row1 = {"Col1": "", "Col2": "", "Col3": ""}
    row2 = {"Col1": "", "Col2": "", "Col3": ""}
    row3 = {"Col1": "", "Col2": "", "Col3": ""}

    while markerchoice1 not in markers:
        markerchoice1 = input("Player 1: Do you want to be X or O? ")

    if markerchoice1 == markers[0]:
        markerchoice2 = markers[1]
    else:
        markerchoice2 = markers[0]

    while not winner:
        if singleplayer:
            userchoice = getuser()
            deloption = str(userchoice[1])+str(userchoice[0][-1])
            delindex = avble.index(deloption)
            if userchoice[1] == "A":
                while row1[userchoice[0]] != "":
                    print("This position is already taken. Please choose another spot.")
                    userchoice = getuser()
                    deloption = userchoice[1] + str(userchoice[0][-1])
                    delindex = avble.index(deloption)
                row1[userchoice[0]] = markerchoice1
                del avble[delindex]
            elif userchoice[1] == "B":
                while row2[userchoice[0]] != "":
                    print("This position is already taken. Please choose another spot.")
                    userchoice = getuser()
                    deloption = userchoice[1] + str(userchoice[0][-1])
                    delindex = avble.index(deloption)
                row2[userchoice[0]] = markerchoice1
                del avble[delindex]
            elif userchoice[1] == "C":
                while row3[userchoice[0]] != "":
                    print("This position is already taken. Please choose another spot.")
                    userchoice = getuser()
                    deloption = userchoice[1] + str(userchoice[0][-1])
                    delindex = avble.index(deloption)
                row3[userchoice[0]] = markerchoice1
                del avble[delindex]

            comchoice = getcom(avble)
            deloption = str(comchoice[1][-1])+str(comchoice[0])
            delindex = avble.index(deloption)
            if comchoice[0] == "A":
                while row1[comchoice[1]] != "":
                    comchoice = getcom(avble)
                    deloption = comchoice[1][-1]+str(comchoice[0])
                    delindex = avble.index(deloption)
                row1[comchoice[1]] = markerchoice2
                del avble[delindex]
            elif comchoice[0] == "B":
                while row2[comchoice[1]] != "":
                    comchoice = getcom(avble)
                    deloption = comchoice[1][-1]+str(comchoice[0])
                    delindex = avble.index(deloption)
                row2[comchoice[1]] = markerchoice2
                del avble[delindex]
            elif comchoice[0] == "C":
                while row3[comchoice[1]] != "":
                    comchoice = getcom(avble)
                    deloption = comchoice[1][-1]+str(comchoice[0])
                    delindex = avble.index(deloption)
                row3[comchoice[1]] = markerchoice2
                del avble[delindex]
        getwin = testwin(row1, row2, row3, winner)
        winner = getwin[0]
        winmark = getwin[1]
        print(winner)
        print(winmark)
        printboard(row1, row2, row3)






main()