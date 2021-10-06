#Independent Programming 3 - Apples
#By: Robert Bayer
#Asks user for a color and flavor of apple and provides the user with the availability of it within the store

#Displays a freindly welcome page for visitors to enjoy
def printWelcome():
    print("""
    Welcome to Papa Party's Apple Black Market!
    We keep a party going so authorities turn a blind eye to our illegal apple trade!
    Disclaimer: if you get caught, and snitch, you're as good as dead...looking at you 6ix9ine...
    """)

#Displays the choices of colors available
def printColorMenu():
    print("""
    Our Color options are...
    Red
    Green
    Other
    """)

#Displays the choices of flavors available
def printFlavorMenu():
    print("""
    Our Flavor Options are...
    Tart
    Sweet
    Mixture
    """)

#Main working function
def main():
    choice = "yes"
    #Form a loop to loop while the decision to continue is yes
    while choice == "yes":
        printWelcome()
        printColorMenu()
        color = input("Please choose a color: ")
        printFlavorMenu()
        flavor = input("Please choose a flavor: ")

        #changing the choices to all lowercase for comparisons
        color = color.lower()
        flavor = flavor.lower()

        #Displays the availability of the apple based on the descriptors
        if color == "green" and flavor == "tart":
            print("The Granny Smith Apple is available for purchase!")
        elif color == "red" and flavor == "sweet":
            print("The Fuji Apple is available for purchase!")
        elif color == "other" and flavor == "mixture":
            print("The Opal Apple is available for purchase!")
        else:
            print("We currently do not have an apple like that, hut you may want to check other stores.")
        choice = input("Do you want to continue? (yes/no): ")
        choice = choice.lower()

main()