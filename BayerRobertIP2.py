#Name: Dr. Justin's Ice Cream Emporium (Independent Program 2)
#Author: Robert Bayer
#Description: Asks for users choice of ice cream from a menu and calucaltes the total before and after taxes

#Define the total price of desired scoops of vanilla
def vanilla(amount, price):
    total = amount * price
    return total

#Define the total price of desired scoops of chocolate
def chocolate(amount, price):
    total = amount * price
    return total

#Define the total price of desired scoops of neapolitan
def neapolitan(amount, price):
    total = amount * price
    return total

#Define the total price of desired scoops of rocky road
def rocky_road(amount,price):
    total = amount * price
    return total

#Define the total price of desired scoops of mint
def mint(amount, price):
    total = amount * price
    return total

#Define the total price of desired scoops of dalted caramel
def salted_caramel(amount, price):
    total = amount * price
    return total

#Calculates the total with tax
def calculate_tax(total, tax):
    grandtotal = total + total * tax
    return grandtotal

#The working function
def main():
    #Setting the Prices of the store
    vanilla_price = 2.90
    chocolate_price = 3.00
    neapolitan_price = 3.15
    rocky_road_price = 3.25
    mint_price = 3.10
    salted_caramel_price = 3.45

    #Welcome Screen (The 0's are there just to make the prices look correct)
    print(f"""

Welcome to Dr. Justin's Ice Cream Emporium!

Please take a look at our menu:
Vanilla: ${vanilla_price}0
Chocolate: ${chocolate_price}0
Neapolitan: ${neapolitan_price}
Rocky Road: ${rocky_road_price}
Mint: ${mint_price}0
Salted Caramel: ${salted_caramel_price}

""")
    #Requesting the desired amount of each ice cream
    vanilla_amount = int(input("How many scoops of Vanilla would you like? "))
    chocolate_amount = int(input("How many scoops of Chocolate would you like? "))
    neapolitan_amount = int(input("How many scoops of Neapolitan would you like? "))
    rocky_road_amount = int(input("How many scoops of Rocky Road would you like? "))
    mint_amount = int(input("How many scoops of Mint would you like? "))
    salted_caramel_amount = int(input("How many scoops of Salted Caramel would you like? "))
    tax = float(input("What is the tax in your area? (Enter value between 0.00 and 1.00): "))

    #restateing the order
    print(f"""
Your order is:
{vanilla_amount} scoops of Vanilla
{chocolate_amount} scoops of Chocolate
{neapolitan_amount} scoops of Neapolitan
{rocky_road_amount} scoops of Rocky Road
{mint_amount} scoops of Mint
{salted_caramel_amount} scoops of Salted Caramel
    """)

    #calculate total without tax
    total_before_tax = vanilla(vanilla_amount, vanilla_price) + chocolate(chocolate_amount, chocolate_price) + neapolitan(neapolitan_amount, neapolitan_price) + rocky_road(rocky_road_amount, rocky_road_price) + mint(mint_amount, mint_price) + salted_caramel(salted_caramel_amount, salted_caramel_price)
    #calculate total with tax
    total_after_tax = calculate_tax(total_before_tax, tax)

    #display the results
    print(f"Your total before tax is ${round(total_before_tax, 2)}")
    print(f"Your total with tax is ${round(total_after_tax, 2)}")
    print("")

    #Hold to see result
    input("Press Enter to Continue...")
    print("")

    #Goodbye Message
    print("Thank you for your money.")
    input("Press Enter to Close...")

#calling the working function
main()



vanilla[1]