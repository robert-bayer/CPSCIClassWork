#Robert Bayer
#Module 7 Class Activity 2

#1

#set the initial number
startNum = 10

#count down until we get to 1
while startNum > 0:
    print(startNum)
    startNum -= 1

#2

#"I'm not going to change" will print over and over again

#3

answer = 0

while answer != 'yes' and answer != 'no':
    answer = input("Please enter yes or no: ")

print("Thank you for entering", answer)