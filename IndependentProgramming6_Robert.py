# Robert Bayer
# Independent Programming 6
"""
fileobj = open("ip6list.txt", "r")
lines = fileobj.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

    peanut butter
    applE jElly
    this is a sAmplE
"""

# The opening welcome to the program, it gives instructions too.
def printwelcome():
    print("""The following program is used to display how many non-vowel characters are in a string.
    
The program will load a file with strings in it, you will then add your own strings when prompted. When you are finished,
type 'q'. The program will then count how many characters in each string are not vowels and present the information to
you as well as save it in a file for later use.

Welcome, and let the games begin.
""")

# This will open the file and return a list of all of the lines
def readfile(filename):
    fileObj = open(filename, "r")
    linelist = fileObj.readlines()
    for i in range(len(linelist)):
        linelist[i] = linelist[i].replace("\n", "")
    fileObj.close()
    return linelist

# This will allow the user to add their own strings to the list
def filllist(prepopulatedlist):
    choice = ""
    origlsit = prepopulatedlist
    # Asks for more inputs
    while choice != "q":
        choice = input("Type another string to add to your list.  If you are finished, type 'q': ")
        # Until q is typed in
        if choice == "q":
            break
        else:
            origlsit.append(choice)
    return origlsit

# This will count all non-vowel characters
def countnonvowel(populatedlist):
    vowel = ["A", "E", "I", "O", "U"]
    results = []
    count = 0
    # For each string
    for item in populatedlist:
        # For each letter in the string
        for letter in item:
            # Tests if it is a vowel
            if letter not in vowel:
                print(letter)
                count += 1
        results.append(count)
        count = 0
    return results

# Puts all of the information into an output file
def outputfile(mylist, results, filename):
    outputfileObj = open(filename, "w")
    # Fixing grammatical mistakes in the sentence
    for item in range(len(mylist)):
        if results[item] == 1:
            outputfileObj.write(f"The string '{mylist[item]}' has {results[item]} character that are not vowels in it.\nBoi")
        elif results[item] == 0:
            outputfileObj.write(f"The string '{mylist[item]}' has only vowels in it.\n")
        else:
            outputfileObj.write(f"The string '{mylist[item]}' has {results[item]} characters that are not vowels in it.\n")

    outputfileObj.write("\n")
    outputfileObj.write(str(mylist))
    outputfileObj.write("\n")
    outputfileObj.write(str(results))
    outputfileObj.close()

#The main working function
def main():
    printwelcome()
    # File names
    file_name = "ip6list.txt"
    outputfilename = "results.txt"

    try:
        mylist = readfile(file_name)

        mylist = filllist(mylist)

        upperlist = []

        # Make everything upper case
        for j in range(len(mylist)):
            upperlist.append(mylist[j].upper())

        results = countnonvowel(upperlist)

        print("""
        
        
        
        
        """)

        for item in range(len(mylist)):
            if results[item] == 1:
                print(f"The string '{mylist[item]}' has {results[item]} character that are not vowels in it.")
            elif results[item] == 0:
                print(f"The string '{mylist[item]}' has only vowels in it.")
            else:
                print(f"The string '{mylist[item]}' has {results[item]} characters that are not vowels in it.")

        outputfile(mylist, results, outputfilename)

    except Exception as e:
        print("There was an issue reading your file, please try again.")
        print(e)

main()