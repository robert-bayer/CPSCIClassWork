#Names: Robert Bayer and Charles Charter
#Date: 4 November 2019
#Description: Simulating a game of Tic Tac Toe

#Asks for the user's choice of block
def userpick(R1, R2, R3, player):
    choice = ["1", "2", "3"]
    R1 = R1
    R2 = R2
    R3 = R3
    UR = ""
    UC = ""
    Uchoice = ""

    #Asks for the row, and if it doesnt exsist, ask again
    UR = input(f"Player {player}: What row do you want (1,2,3): ")
    while UR not in choice:
        print("That space does not exist.")
        UR = input(f"Player {player}: What row do you want (1,2,3): ")
    UR = int(UR)

    #Asks for the column, and if it doesnt exsits, ask again
    UC = input(f"Player {player}: What Column do you want(1,2,3): ")
    while UC not in choice:
        print("That space does not exist.")
        UC = input(f"Player {player}: What Column do you want(1,2,3): ")
    UC = int(UC)

    #Sees if the space is empty
    if UR == 1:
        Uchoice = R1[f"C{UC}"]
    elif UR == 2:
        Uchoice = R2[f"C{UC}"]
    elif UR == 3:
        Uchoice = R3[f"C{UC}"]

    #If the spot is already taken, ask for the row and column again
    while Uchoice != "":
        print("That space is already taken...")
        UR = ""
        UC = ""
        Uchoice = ""
        UR = input(f"Player {player}: What row do you want (1,2,3): ")
        while UR not in choice:
            print("That space does not exist.")
            UR = input(f"Player {player}: What row do you want (1,2,3): ")
        UR = int(UR)

        UC = input(f"Player {player}: What Column do you want(1,2,3): ")
        while UC not in choice:
            print("That space does not exist.")
            UC = input(f"Player {player}: What Column do you want(1,2,3): ")
        UC = int(UC)

        #sees if the space is empty
        if UR == 1:
            Uchoice = R1[f"C{UC}"]
        elif UR == 2:
            Uchoice = R2[f"C{UC}"]
        elif UR == 3:
            Uchoice = R3[f"C{UC}"]

    return UR, UC

#testing to see if someone has won
def wincond(row1, row2, row3):
    row1 = row1
    row2 = row2
    row3 = row3
    winner = False
    winmark = None

    #all of the win conditions
    if (row1["C1"] == row2["C1"] == row3["C1"]) and (row1["C1"] != ""):
        winner = True
        winmark = row1["C1"]
    elif (row1["C2"] == row2["C2"] == row3["C2"]) and (row1["C2"] != ""):
        winner = True
        winmark = row1["C2"]
    elif (row1["C3"] == row2["C3"] == row3["C3"]) and (row1["C3"] != ""):
        winner = True
        winmark = row1["C3"]
    elif (row1["C1"] == row1["C2"] == row1["C3"]) and (row1["C1"] != ""):
        winner = True
        winmark = row1["C1"]
    elif (row2["C1"] == row2["C2"] == row2["C3"]) and (row2["C1"] != ""):
        winner = True
        winmark = row2["C1"]
    elif (row3["C3"] == row3["C2"] == row3["C3"]) and (row3["C1"] != ""):
        winner = True
        winmark = row3["C3"]
    elif (row1["C1"] == row2["C2"] == row3["C3"]) and (row1["C1"] != ""):
        winner = True
        winmark = row1["C1"]
    elif (row3["C1"] == row2["C2"] == row1["C3"]) and (row3["C1"] != ""):
        winner = True
        winmark = row3["C1"]
    else:
        winner = False
        winmark = None
    return winner, winmark

#prints the board with the players marks
def printboard(row1, row2, row3):

    print(f"""
        |        |
\t{row1["C1"]}\t|\t{row1["C2"]}\t |\t{row1["C3"]}       
________|________|________
        |        |
\t{row2["C1"]}\t|\t{row2["C2"]}\t |\t{row2["C3"]} 
________|________|________
        |        |
\t{row3["C1"]}\t|\t{row3["C2"]}\t |\t{row3["C3"]} 
        |        |    
    """)

#the main working function
def main():
    player1 = "X"
    player2 = "O"
    R1 = {"C1": "", "C2": "", "C3": ""}
    R2 = {"C1": "", "C2": "", "C3": ""}
    R3 = {"C1": "", "C2": "", "C3": ""}

    #gets the initial win condition
    wincondition = wincond(R1, R2, R3)
    win = wincondition[0]
    winner = wincondition[1]

    #While there is no winner, play the game
    while not win:
        #get player one's choice
        userchoice1 = userpick(R1, R2, R3, 1)
        UR1 = userchoice1[0]
        UC1 = userchoice1[1]

        #sets the space to player one's mark
        if UR1 == 1:
            R1[f"C{UC1}"] = "X"
        if UR1 == 2:
            R2[f"C{UC1}"] = "X"
        if UR1 == 3:
            R3[f"C{UC1}"] = "X"

        #retest if there is a new winner
        wincondition = wincond(R1, R2, R3)
        win = wincondition[0]
        winner = wincondition[1]
        #if player one won, break the loop
        if win:
            break

        #display board to show available spaces
        printboard(R1, R2, R3)

        #get player two's choice
        userchoice2 = userpick(R1, R2, R3, 2)
        UR2 = userchoice2[0]
        UC2 = userchoice2[1]

        #sets the space to player two's mark
        if UR2 == 1:
            R1[f"C{UC2}"] = "O"
        if UR2 == 2:
            R2[f"C{UC2}"] = "O"
        if UR2 == 3:
            R3[f"C{UC2}"] = "O"

        #retests to see if there is a new winner
        wincondition = wincond(R1, R2, R3)
        win = wincondition[0]
        winner = wincondition[1]

        #displays board and empty spaces
        printboard(R1, R2, R3)

    #Tells the win statement and who won
    print(f"{winner} wins!")
    printboard(R1, R2, R3)

main()