#Robert Bayer
#Independent Programming 5
#
from pip._vendor.distlib.compat import raw_input


def print_welcome():
    print("""
Welcome to the string check program
This program checks if your string meets the following criteria:
1. Contains only one special character
2. Is at least 8 characters long
3. Has at least one capital letter
4. Has at least two numbers
5. One of the minimum two numbers must be a 0

When prompted, input your string and press enter.
To quit just type 'q' when prompted for the string.
""")


def verify_password(mystring):
    success = {"special": 1, "length": True, "cap": True, "nums": True, "zero": True}
    verify = {"special": 0, "length": False, "cap": False, "nums": False, "zero": False}
    nums = 0
    if len(mystring) < 8:
        return "does not meet the criteria"
    else:
        verify["length"] = True
        for char in mystring:
            if char == "!" or char == "@" or char == "#" or char == "$" or char == "%" or char == "^" or char == "&" or char == "*" or char == "(" or char == ")":
                verify["special"] += 1
            if char.upper() == char:
                verify["cap"] = True
            if char.isdigit() == True:
                nums += 1
                number = int(char)
                if number == 0:
                    verify["zero"] = True
        if nums >= 2:
            verify["nums"] = True
        if verify == success:
            return "meets the criteria"
        else:
            return "does not meet the criteria"


def main():
    string = ""
    while string != "q":
        userstring = raw_input("Please input your string or input 'q' to quit: ")
        if userstring == "q":
            print("Thanks for playing!")
            break
        print(userstring, verify_password(userstring))



main()