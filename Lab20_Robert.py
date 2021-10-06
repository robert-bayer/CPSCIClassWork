#Lab 20
#Robert Bayer
#Manipulate a list of books for reading

#Menu full of options
def printMenu():
    print("""
    List All (L)
    Add (A)
    Number of Books (N)
    Remove (R)
    Insert (I)
    Quit (Q)
    """)

#Prints the list of books
def printList(mylist):
    if len(mylist) == 0:
        print("<<No Titles in List>>")
    else:
        for i in mylist:
            print(i)

def main():
    readingList = ["Catch 22", "Time Machine"]
    print("Welcome to the reading list thing.")
    x = 0
    #gives the options that a user can input
    options = ["L", "l", "A", "a", "N", "n", "R", "r", "I", "i", "Q", "q"]
    #repeats the request until a valid input is given
    while x not in options:
        printMenu()
        x = input("Please Input your choice: ")
    #Does the chose request
    while (x in options) and (x != "Q" or x != "q"):
        while x not in options:
            printMenu()
            x = input("Please Input your choice: ")
        #Lists the books
        if x == "L" or x == "l":
            printList(readingList)
            printMenu()
            x = input("Please Input your choice: ")
        #Adds a book on the end of the list
        elif x == "A" or x == "a":
            y = input("Please input the title of another: ")
            readingList = readingList + [y]
            printMenu()
            x = input("Please Input your choice: ")
        #Gives the number of books
        elif x == "N" or x == "n":
            print(len(readingList))
            printMenu()
            x = input("Please Input your choice: ")
        #Removes a book from the list
        elif x == "R" or x == "r":
            r = input("Please input a title to remove: ")
            if r in readingList:
                h = readingList.index(r)
                del readingList[h]

            else:
                print("There is no book with that title in the reading list")
            printMenu()
            x = input("Please Input your choice: ")
        #Inserts a book at the given index
        elif x == "I" or x == "i":
            i = input("Enter a title to input: ")
            ind = int(input("Enter what index to insert: "))
            while i in readingList:
                print("Sorry, that book is already in the list.")
                i = input("Enter a title to input: ")
            while ind < 1 or ind > (len(readingList) - 1):
                print("Sorry, that index is invalid")
                ind = int(input("Enter at what index to insert: "))
            readingList = readingList[:ind] + [i] + readingList[ind:]
            printMenu()
            x = input("Please Input your choice: ")
        #Closes the program
        elif x == "Q" or x == "q":
            print("Bye")
            break

    print("")
    print("End of Program")

main()