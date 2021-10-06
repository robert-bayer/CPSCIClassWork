#Lab18
#Robert Bayer

print("""

0 Choice 1
1 Choice 2
2 Choice 3
3 Choice 4
4 Choice 5
5 Choice 6

""")



string = input("Enter a number (0-5): ")

if string.isdigit() == False:
    string = 100
else:
    string = int(string)

while string < 0 and string > 5:
    string = input("Enter a valid number (0-5): ")
    if string.isdigit() == False:
        string = 100
    else:
        string = int(string)

if string == 0:
    do this
elif string ==1:
    do this
elif string == 2:
    do this
elif string ==3:
    do this
elif string == 4:
    do this
elif string == 5:
    do this