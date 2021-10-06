def displayStars(x):
    for i in range(x):
        for j in range(x, i+1, -1):
            print(" ", end="")
        for g in range(i+1):
            print("#", end="")
        print("  ", end="")
        for h in range(i+1):
            print("#", end="")
        for l in range(x, i+1, -1):
            print(" ", end="")
        print()

x = int(input("How tall do you want your pyramid: "))
print("Here is your pyramid!")
displayStars(x)