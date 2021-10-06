def main():
    x = int(input("Type your favorite number: "))
    y = int(input("Type your next favorite number: "))
    if x % y == 0:
        print("You are wise beyond your years...")
    else:
        print("You will fail an enumerous times...")

    if x // y > 5:
        print("You will be very successful...")
    else:
        print("I hope the back of your car is comfortable...")

    if x == y:
        print("You are lame...")
    if x != y:
        print("Goodbye")

main()