#imports random module for use of random functions
import random

#this function orders the items with price and how many items as parameter to calc price
def orderTShirt(tShirtPrice, quantity):
    total = tShirtPrice * quantity
    return round(total, 2)

# this function orders the items with price and how many items as parameter to calc price
def orderLongSleeve(longPrice, quantity):
    total = longPrice * quantity
    return round(total, 2)

#this function calculates tax percent
def calculateTax(taxPercent, total):
    trueTotal = taxPercent * total + total
    return round(trueTotal, 2)

# this function orders the items with price and how many items as parameter to calc price
def orderHoodie(hoodiePrice, quantity):
    total = hoodiePrice * quantity
    return round(total, 2)

#this function will create a random price for a single item
def createPrice():
    newPrice = random.uniform(.5, 18)
    newPriceRounded = round(newPrice, 2)
    return newPriceRounded

#this function prints a welcome statement
def welcome():
    print("Hello! Welcome to the Shirt Shop!")

#this function carries all code that isn't import
def main():
    welcome()

    tax = .08

    tShirtPrice = createPrice()
    longPrice = createPrice()
    hoodiePrice = createPrice()

    numTshirt = int(input("Please enter how many T-Shirts you want to buy: "))
    numLongSleeve = int(input("Please enter how many Long Sleeve Shirts you want to buy: "))
    numHoodie = int(input("Please enter how many Hoodies you want to buy: "))

    totalTShirt = orderTShirt(tShirtPrice, numTshirt)
    totalLSleeve = orderLongSleeve(longPrice, numLongSleeve)
    totalHoodie = orderHoodie(hoodiePrice, numHoodie)

    totalPreTax = totalTShirt + totalLSleeve + totalHoodie
    totalPreTax = round(totalPreTax, 2)

    totalPostTax = calculateTax(tax, totalPreTax)

    print("Your order of " + str(numTshirt) + " T-Shirts costs $" + str(totalTShirt) +".")
    print("Your order of " + str(numLongSleeve) + " Long Sleeves costs $" + str(totalLSleeve) + ".")
    print("Your order of " + str(numHoodie) + " Hoodies costs $" + str(totalHoodie) + ".")

    print("Your total before tax is $" + str(totalPreTax) + ".")
    print("Your total after tax is $" + str(totalPostTax) + ".")

#call main function to start program
main()