#Name: Rock, Scissors, Paper
#Author: Robert Bayer
#Date: 9/9/2019
#Description: A game of Scissors, Rock, Paper

#Import needed modules
import random

#Defining a function that gets the computer's choice
def AI():
    AIPick = random.randint(1,3)
    return AIPick

#Defining a function that determines who is the winner and gives them a point
def Winner(userPick, AIPick):
    userScore = 0
    AIScore = 0
    if userPick == AIPick:
        print("Tie!")
    elif userPick == 1 and AIPick == 3:
        print("You Win!")
        userScore += 1
    elif userPick == 2 and AIPick == 1:
        print("You Win!")
        userScore += 1
    elif userPick == 3 and AIPick == 2:
        print("You Win!")
        userScore += 1
    else:
        print("The Computer Wins!")
        AIScore += 1
    return userScore, AIScore

#The main functions
def main():
#Get the users choice
    userPick = input("""
    1 for Rock
    2 for Paper
    3 for Scissors
    q for Quit
    
    """)
#Get the computer's choice
    AIPick = AI()


#Set initial score
    userScoreFinal = 0
    AIScoreFinal = 0

#Loops the game
    while userPick != "q" or AIScoreFinal != 5 or userScoreFinal !=5:
        userPick = int(userPick)
        #Repeats it if user gives invalid choice
        while userPick > 3 or userPick < 1:
            userPick = int(input("""
                        1 for Rock
                        2 for Paper
                        3 for Scissors
                        
                        """))
        AI()
        #Tests choices
        x = Winner(userPick, AIPick)
        #Update scores
        userScoreFinal += x[0]
        AIScoreFinal += x[1]
        #Print results
        print("Computer's Score: ", AIScoreFinal)
        print("Your Score: ", userScoreFinal)
        #repeat
        userPick = input("""
            1 for Rock
            2 for Paper
            3 for Scissors
            q for Quit
            
            """)

        AIPick = AI()
    #Quit condition
    if userPick == "q":
        print("Goodbye!")

#Run the game
main()