#Independent Prograing Practice
#Robert Bayer


def welcome():
    print("""
Welcome to the plastic identification project
Our goal is to make consumers more aware about what different types of plastic are used for
Please input a number when prompted to get the facts and information on your plastic!
""")

def userinput():
    x = input("Please enter the number within the triangle on your plastic: ")
    if x.isdigit() == False:
        x = "100"
        x = int(x)
    else:
        x = int(x)

    while x <= 0 or x >= 8:
        print("I'm sorry, that classification doesn't exsist, please enter a number 1-7")
        x = input("Please enter the number within the triangle on your plastic: ")
        if x.isdigit() == False:
            x = "100"
            x = int(x)
        else:
            x = int(x)
    return x


def plasticChoice(rating):
    if rating == 1:
        return """PET is intended for single use. Reusing increases the risk of carcinogen leaching and bacterial growth.
         PET is difficult to decontaminate. Recycle but don’t reuse."""
    elif rating == 2:
        return """HDPE is one of the safest forms of plastic. Resistant to heat and cold. Can be reused and recycled. """

    elif rating == 3:
        return """PVC is relatively impervious to sunlight and weather. It contains numerous toxins that can leach 
    throughout the lifecycle of the plastic. Cannot be recycled. Can be reused."""

    elif rating == 4:
        return """LDPE is relatively safe for use. Reusable but not always recyclable. """

    elif rating == 5:
        return """PP is heat-resistant and acts as a barrier against moisture, grease, and chemicals. Can be reused and 
    recycled."""

    elif rating == 6:
        return """PS is inexpensive and lightweight. Leaches carcinogens and breaks up easily. Low market for recycling 
    and difficult to reuse. Should be avoided."""

    elif rating == 7:
        return """PC and “other” plastics. These vary which is confusing for consumers. Because of concerns with carcinogen
     leaching, avoid these unless it also contains the letters PLA or Compostable. These are made from bio-based
     polymers that can be composted."""

def main():
    cont = "y"
    welcome()
    while cont == "y":
        rating = userinput()

        print(f"For plastic with the rating of {rating}:", plasticChoice(rating))
        cont = input("Do you want to continue? (y/n) ")

main()