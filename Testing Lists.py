#Programming Project 6 - Lists
#Robert Bayer
#Gets a 7 Digit Number from the user and presents all combinations of characters associated with those numbers

#Gets a number from the user
def getnum():
    numberlist = []
    number = "00000000"
    #gets the proper length of number
    while len(number) != 7:
        number = input("Enter a seven number digit: ")
    #turns the number into a list to make it easier to parse
    for i in number:
        i = int(i)
        numberlist += [i]
    return numberlist

#takes each of the entries in the number's list and cycles through each one present all possible character combinations
def combos(numberlist):
    #list of all letters associated with each number
    nums = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"],
            ["P", "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y", "Z"]]
    #list of numbers that will actually return a letter
    accept = [2,3,4,5,6,7,8,9]
    word = ""
    result = []
    #the loop that cycles through each character at each level
    for k in nums[numberlist[0]-2]:
        for l in nums[numberlist[1]-2]:
            for m in nums[numberlist[2]-2]:
                for n in nums[numberlist[3]-2]:
                    for o in nums[numberlist[4]-2]:
                        for p in nums[numberlist[5]-2]:
                            for q in nums[numberlist[6]-2]:
                                #These if statements replace any 1 or 0 with a blank character spot
                                if numberlist[0] not in accept:
                                    k = " "
                                if numberlist[1] not in accept:
                                    l = " "
                                if numberlist[2] not in accept:
                                    m = " "
                                if numberlist[3] not in accept:
                                    n = " "
                                if numberlist[4] not in accept:
                                    o = " "
                                if numberlist[5] not in accept:
                                    p = " "
                                if numberlist[6] not in accept:
                                    q = " "
                                #building the "word"
                                word = k + l + m + n + o + p + q
                                #adding the word to a list
                                result += [word]
                                #resetting the word variable
                                word = ""
    return result

#main working function
def main():
    cont = "y"
    #sets a loop to continue for as any times as wanted
    while cont == "y":
        #gets the numlist and sets it where it can be accessed
        numlist = getnum()
        #gets the list of results to an accessible level
        results = combos(numlist)
        #prints the results on their own line
        for i in results:
            print(i)
        #asks if user wants to do it again
        cont = input("Do you want to continue? (y/n): ")


#calling the main working function
main()