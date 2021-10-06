#Name: Dumbscrum Court Paint Cost Calculator
#By: Robert Bayer
#Date: 8/21/2019
#Description: This program is to be used to calculate the amount of
#             paint needed to pain the hexagonal region the appropriate color

#import needed modules
import math

#Defining variables and constants
paint_per_sqrft = 0.1
side_length = 0
price_of_paint = 0

#Asks user for the price of paint per gallon
side_length = float\
    (input("Enter the length of the sides of the hexagon in feet: "))

#DEBUG
#print("side length: ", side_length)

#Asks user for the length of each side of the hexagon
price_of_paint = float(input("Enter the price of paint per gallon: "))

#DEBUG
#print("price of paint: ", price_of_paint)

#Calculates the area of the hexagon
half_perimeter = (side_length * 3) / 2
triangle_area = math.sqrt(half_perimeter * ((half_perimeter - side_length) ** 3))
hexagon_area = triangle_area * 6

#DEBUG
#print("half perimeter: ", half_perimeter)
#print("triangle area: ", triangle_area)
#print("hexagon area: ", hexagon_area)

#How much paint is needed?
paint_needed = hexagon_area * paint_per_sqrft

#DEBUG
#print("paint needed: ", paint_needed)

#Mow much will that cost?
total_cost = paint_needed * price_of_paint

#DEBUG
#print("total cost: %.2f" % total_cost)

#Return the estimated cost of paint.
print(f"The estimated cost of paint for a hexagon with a side length of {side_length} feet ({hexagon_area} sq ft) would be $ %.2f" % total_cost)

input("Press 'Enter' to close the program...")