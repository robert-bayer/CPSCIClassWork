#Name: Lab 7 Practice Work
#Author: Robert Bayer
#Description: A pound to kilogram converter and a runway length calculator

#Ask for weight in pounds to be converted
pounds = float(input("Please input the amount of pounds to be converted to kilograms..."))
#Calculate the weight in kilograms
kg = pounds / 2.2046
#print results and hold
print (f"{pounds} lbs equals {kg} kilograms")
input("Press Enter to Continue...")


#Ask for the acceleration
accel = float(input("Enter the acceleration value of the plane in meters per second per second: "))
#Ask for the Take off speed
speed = float(input("Enter the take off speed in meters per second: "))
#Calculate minimum runway length
length = (speed ** 2) / (2 * accel)
#print results and hold
print(f"You would need a runway that is at least {length} meters long.")
input("Press Enter to Close...")