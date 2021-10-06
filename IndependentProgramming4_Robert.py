#Independent Programming 4
#Robert Bayer
#Prompts user for a choice in lessons and gives the lesson with a random example from a list of 3 examples

import random

#prints the welcome page
def printWelcome():
    print("""
    
    Welcome to Papa Party's Python Playground!
    Today we will be learning about types of data!
    
    Today's lessons are:
    1. Integers
    2. Floats
    3. Strings
    4. Lists
    5. Dictionaries
    
    Enter 6 when asked for your choice to quit the program.
    
    """)

#Validatest the user's chosen option if it is an acceptable number or not
def inputValidation(choice):
    responses = [1, 2, 3, 4, 5, 6]
    if choice.isdigit():
        choice = int(choice)
        if choice in responses:
            return True
        else:
            return False
    else:
        return False

#Gets the chosen lesson from the list
def getLesson(choice):
    lessons = ["Integer – Signed integer used in the format of ", "Float – Floating point real numbers used in the format of",
               "String – Letters or other characters as a word used in the format of", "Lists – A container of a series of values used in the format of",
               "Dictionary – Lists of Key:Value pairs used in the format of"]
    return lessons[choice]

#Gets a random example from the lesson from the lists
def getExample(choice):
    example = random.randint(0,2)
    examples = [["x = 10", "y = -12","n = 0"],
                ["x = 41.34", "g = 0.01", "u = -4.34"],
                ["x = \"Hello World\"", "string = \"word\"", "name = \"Justin\""],
                ["x = [10, 41.34, \"Hello World\"]", "list1 = [\"\"]", "nums = [1,2,3]"],
                ["x = {\"key\" : \"value\", \"key2\" : \"value2\"}",
                 "d = {\"cost1\" : 3.99, \"cost2\" : 1.00}", "qwe = {1 : 100}"]]
    return examples[choice][example]

#The main working function
def main():
    printWelcome()
    cont = "y"
    contaccept = ["y","n"]
    #Filters out invalid inputs and prompts for another input
    while cont not in contaccept:
        print("Invalid input")
        cont = input("Do you want to continue? (y/n)")
    #Loops while wanting to continue
    while cont == contaccept[0]:
        choice = '0'
        #loops while the chosen lesson is not valid
        while not inputValidation(choice):
            choice = input("Please input your choice of lesson: ")
        choice = int(choice)
        choice -= 1
        #quits if 6 is chosen
        if choice == 5:
            break
        #gets desired lesson and example
        else:
            lessonresult = getLesson(choice)
            exampleresult = getExample(choice)
            print("Ahhh, good choice!")
            #prints the results
            print(lessonresult, exampleresult, sep=" ")
            cont = input("Do you want to continue? (y/n) ")
            #filters out invalid inputs
            while cont not in contaccept:
                print("Invalid input")
                cont = input("Do you want to continue? (y/n)")

#calling the main working function
main()