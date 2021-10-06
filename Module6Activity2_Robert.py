def smallest_int(x,y,z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    else:
        return z

x = int(input("Enter your first integer: "))
y = int(input("Enter your second integer: "))
z = int(input("Enter your third integer: "))

print(smallest_int(x, y, z))

rightMsg = "Yeah, that was fun!"
wrongMsg = "What was it and what question could extend this game?"

print("Think of an animal")

response = input("Does it fly? (yes/no) ")
if response == "yes":
    response = input("Is it black? (yes/no) ")
    if response == "yes":
        response = input("Is it a raven? (yes/no) ")
        if response == "yes":
            print(rightMsg)
        else:
            print(wrongMsg)
    else:
        response = input("Is it an eagle? (yes/no) ")
        if response == "yes":
            print(rightMsg)
        else:
            print(wrongMsg)
else:
    response = input("Does it run really fast? (yes/no) ")
    if response == "yes":
        response = input("Does it have a beak? (yes/ no)")
        if response == "yes":
            response = input("Is it a roadrunner? (yes/no) ")
            if response == "yes":
                print(rightMsg)
            else:
                print(wrongMsg)
        else:
            response = input("Is it a cheetah? (yes/no) ")
            if response == "yes":
                print(rightMsg)
            else:
                print(wrongMsg)
    else:
        print(wrongMsg)

for i in range(59,100+1):
    print(f"{i}% is an ", end="")
    if i == 59:
        print("'F'")
        print("")
    elif i == 69:
        print("'D'")
        print("")
    elif i == 79:
        print("'C'")
        print("")
    elif i == 89:
        print("'B'")
        print("")
    elif i >= 90:
        print("'A'")
    elif 90 > i >= 80:
        print("'B'")
    elif 80 > i >= 70:
        print("'C'")
    elif 70 > i >= 60:
        print("'D'")
    else:
        print("'F'")