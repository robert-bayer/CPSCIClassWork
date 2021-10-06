#Name: Gas N' Go!
#Author: Robert Bayer
#Description: Calculate the cost of gas for 100 miles and how far a car can go on with the amount of their gas.

#Welcome
print("Let's take a look at what's in your tank...")
input("Press Enter to continue...")

print("Let's Start with how many gallons you currently have in your tank.")
gallons_in_tank = float(input("Enter your answer in gallons: "))


print("Awesome! Now what is your average fuel effiency?")
fuel_effiency = float(input("Enter your answer in miles per gallon: "))



print("Great! Now how much is gas in your area?")
gas_price = float(input("Enter your answer in dollars and cents ($X.XX): "))


print("Fantastic! Now, how far away (in miles) are you planning on travelling?")
distance = float(input("Enter your answer in miles: "))


#Cost Per 100 Mile
gallons_for_100 = 100 / fuel_effiency
cost_for_100 = gallons_for_100 * gas_price

#How far you can go with the fuel in the tank
distance_in_tank = gallons_in_tank * fuel_effiency

#answers
print("It costs $%.2f per 100 miles." % cost_for_100)
print(f"You can go {distance_in_tank} before you run out of gas.")

#Hold for result
input("Press Enter to close the program...")