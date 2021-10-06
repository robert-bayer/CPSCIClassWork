def main():
    code = input("Please enter the current code color: ")
    code = code.upper()
    if code == "RED":
        for i in range(50):
            print("RED ALERT!!!")
        x = int(input("Enter the water level: "))
        if x >= 12:
            for g in range(50):
                print("FLOOD WARNING!!!! GET OUT NOW!!!")
        else:
            for h in range(50):
                print("FLOOD WATCH!!!! KEEP AN EYE OUT AND REPORT ANYTHING ASAP!!!!")
    else:
        print("Just chill...")

main()