#Module 6 Project Part 1
#Task A
#Author: Robert Bayer
#Description: Ask for a string, invert the string, print the inverted string

#Define the function to reverse a given string
def reverseScript(myScript):
#Easier one line solution
#    that_string = that_string[::-1]
#    print(that_string)
    x = len(myScript)
    reverse_string = ""
    for i in range(x-1, -1, -1):
        reverse_string += myScript[i]
    return reverse_string



#ask for a string
that_string = input("Enter your secret message: ")

#print the result
print(reverseScript(that_string))
input("Press Enter to Continue")

#Bob doesnt need a seperate program because this will also reverse reversed strings