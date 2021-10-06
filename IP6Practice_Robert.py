#Independient Programming 6 Practice
#Robert Bayer
#This program will import a file, and have a user input strings.  It will then count the number of non-alphetical
#characters are in the string and return them each as an item in a list.

#prints the welcome message
def printwelcome():
    print("Welcome to Justin is being a little meany head and won't let us make any noise or else he will get mad.")
    print("In this program we will be taking strings and count how many non alphabetical characters are in a string and")
    print("return what characters they are and in what index they are held in.")
    print("")

#reads the file and returns each line as an entry in a list
def readfile(infile):
    InputFileObj = open(infile, "r")
    linelist = InputFileObj.readlines()
    return linelist

#Asks the user to add to the list until they type 'q'
def filllist(linelist):
    lines = linelist
    choice = ""
    while choice != "q":
        choice = input("What do you want to add to the list? (To quit, type 'q'): ")
        if choice == "q":
            break
        lines.append(choice)
    return lines

#counts the number of non-alphabetical characters are in each string and adds them as an entry in a list.
def countnonalph(linelist):
    lines = linelist
    totals = []
    count = 0
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
    for string in lines:
        for character in string:
            if not character.isalpha():
                count += 1
        totals.append(count)
        count = 0
    return totals

#main working function
def main():
    file = "ip6practice.txt"
    printwelcome()
    lines = readfile(file)
    lines = filllist(lines)
    nonalpha = countnonalph(lines)
    print("")
    for item in range(len(lines)):
        print(f"{lines[item]}: {nonalpha[item]}")

#calls the main working function
main()