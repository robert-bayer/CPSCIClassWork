#Name: Cash to Couch
#Author: Robert Bayer
#Date: 8/28/2019
#Description: Asks user for commission rate and commission earned and calculates the value of the house.

#Welcome Screen
print("""
Hello, and welcome to Cash to Couch...
We are going to tell you the price of the house based on the information you give us...
Press Enter to Begin!
""")

#Hold
input()

#Ask for commission rate and change it to a float number
rate = float(input("Please input your commission rate in percent (0-100): "))
rate_10 = rate / 100

#Ask for commission received
commission = float(input("Please input your commission earned in dollars: "))

#Find value of the house
house_value = commission / rate_10

#Find number of $500 bonuses recieved
bonus = house_value // 15000

#Find dollar amount of that many bonuses
bonus_money = bonus * 500

#Add bonus amount to commission amound to find new commission total
commission_total = commission + bonus_money

#Show results of calculations
print(f"""According to the information given, the house you sold was valued at ${house_value} This means that you have 
earned a bonus of ${bonus_money}. As a result, your new commission total is $%.2f
"""  % commission_total)

#Hold for end results
input("Press Enter to Close Program...")