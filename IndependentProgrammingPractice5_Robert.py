#Independent Programming 5
#Robert Bayer
#Validating passwords
from pip._vendor.distlib.compat import raw_input


def printWelcome():
    print("""
Welcome to the string check program
This program checks if your string meets the following criteria:
1. Contains at least one asterisk (*)
2. Does not have any numbers
3. Has exactly one j (upper or lower case)
4. Has at least one P (upper case)
""")


def noNumOneJhasAstP(mystring):
    correct = {"Ast": True, "Nums": True, "j": True, "P": True}
    valid = {"Ast": False, "Nums": True, "j": False, "P": False}
    if "*" in mystring:
        valid["Ast"] = True
    if "P" in mystring:
        valid["P"] = True
    for char in mystring:
        if char.isdigit() == True:
            valid["Nums"] = False
        if (char == "j" or char == "J") and valid["j"] == False:
            valid["j"] = True
        elif (char == "j" or char == "J") and valid["j"] == True:
            valid["j"] = False
    if valid == correct:
        return f"{mystring} meets the criteria"
    else:
        return f"{mystring} does not meet the criteria"


def main():
    userinput = 1
    while userinput != "q":
        userinput = raw_input("Enter a password to continue, enter 'q' to quit: ")
        while userinput == "":
            userinput = raw_input("Enter a password to continue, enter 'q' to quit: ")
        if userinput == "q":
            break
        else:
            print(noNumOneJhasAstP(userinput))

main()