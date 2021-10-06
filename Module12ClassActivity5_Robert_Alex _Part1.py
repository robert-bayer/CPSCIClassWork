#Module 12 Class Activity 5
#Robert Bayer
#The Program will search for an address based on if a argument is passed through command prompt, and if not then based on user input.
import sys
import pyperclip as pc
import webbrowser as wb


def grabaddress():
    address = pc.paste()
    return address

def useraddress():
    address = input("What address would you like? ")


def main():
    #grab the address
    if len(sys.argv) > 1:
        myaddr = ' '.join(sys.argv[1:])
    else:
        choice = ""
        while choice != "user" and choice != "clipboard":
            choice = input("If you want the program to grab the website from the clipboard, type 'clipboard' ."
                           "Else, if you want to type in your own address, type 'user'. "
                           " ")
        if choice == "clipboard":
            try:
                myaddr = grabaddress()
            except:
                print("You don't have an address copied.")
        elif choice == "user":
            myaddr = input("Please type in your address now: ")

#138 Rose Anne Loop, Hamilton, GA 31811
#https://www.google.com/maps/place/138+Roseanne+Loop,+Hamilton,+GA+31811
    #request google maps
    wb.open('https://google.com/maps/place/' + myaddr)

#TO OPEN MULTIPLUE TABS:
#URL1 = "www.xyz.com"
#URL2 = "www.zyx.com"

#wb.open_new_tab(URL1)
#wb.open_new_tab(URL2)

main()
