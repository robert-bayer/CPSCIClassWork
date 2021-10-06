#Independent Programming 4
#Robert Bayer
#Gives facts on animals based on user choice


def print_welcome():
    print("""
    Howdy, we are talking about animals today.  I hope you're ready to learn at Dr. Lesh's funny farm!
    """)


def input_validation():
    choice = " "
    accept = ["1", "2", "3", "4", "5"]
    while choice not in accept:
        choice = input("Please input a number (1, 2, 3, 4, 5): ")
    choice = int(choice)
    return choice


def what_fact(choice):
    facts = ["1.     An octopus is a highly intelligent invertebrate and a master of disguise",
             "2.     Elephants have the largest brain of any land animal and three times as many neurons as humans",
             "3.     African Grey Parrots are capable of abstract logical reasoning",
             "4.     Whales and dolphins have specialized neurons associated with advance abilities such as recognizing, remembering, reasoning, communicating, perceiving, adapting to change, and understanding",
             "5.     Crows and other corvids have incredible memories and can remember human faces"
            ]

    if choice == 1:
        return facts[0]
    elif choice == 2:
        return facts[1]
    elif choice == 3:
        return facts[2]
    elif choice == 4:
        return facts[3]
    else:
        return facts[4]


def main():
    contchoice = ["y", "n"]
    cont = "y"
    print_welcome()
    while cont not in contchoice:
        cont = input("Do you want to continue? (y/n) ")
    while cont == contchoice[0]:
        choice = input_validation()
        print(what_fact(choice))
        cont = input("Do you want to continue? (y/n) ")
        while cont not in contchoice:
            cont = input("Do you want to continue? (y/n) ")


main()
