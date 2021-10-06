



def simple_calc():
    operand = input("Enter your desired operation: ")
    x = int(input("Enter your first operand: "))
    y = int(input("Enter your second operand: "))

    if operand == "+":
        z = x + y
        print(z)
    elif operand == "-":
        z = x - y
        print(z)
    elif operand == "*":
        z = x * y
        print(z)
    elif operand == "/":
        z = x / y
        print(z)
    else:
        print("Invalid operation")

