#Name: Encryptor, Decryptor
#Author: Robert Bayer (With assistance from Justin Lesh)
#Description: Based on input from the user, the program will encrypt or decrypt a given string with a provided key chosen at the time of encryption


#shifts the alphabet and reprints the string in the new alphabet
def alpha_shift(string, coding_mode):
    new = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    number = int(input("Enter a number between 1 and 25 (This is your key): "))

    #Decides what to do depending on whether or not it is decoding or encoding
    if coding_mode == 1:
        for i in string:
            #keeps special characters and spaces
            if i not in alpha:
                new += i
            else:
                inx = alpha.find(i)
                inx += number
                inx = inx % 26
                new += alpha[inx]
        return new, number
    else:
        for i in string:
            if i not in alpha:
                new += i
            else:
                inx = alpha.find(i)
                inx -= number
                inx = inx % 26
                new += alpha[inx]
        return new, number

#reverses the given string
def reverse_string(string):
    stringreversed = string[::-1]
    return stringreversed

#main working function
def main():
    #Asks if they are encoding or decoding
    coding_mode = int(input("Enter 1 if you are encoding, enter 2 if you are decoding: "))
    #Asks for the string they are decoding
    x = input("Enter a string: ")
    x = x.lower()
    n = reverse_string(x)
    m = alpha_shift(n,coding_mode)
    result = m[0]
    resultnum = m[1]
    #prints the results
    print(f"Your message: {result}                  Your key: {resultnum}")

main()