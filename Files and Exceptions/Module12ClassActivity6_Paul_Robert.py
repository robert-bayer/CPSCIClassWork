#Module 12 Class Activity 6
#Paul Carroll and Robert Bayer

###High Level###
#take the thing we are supposed to decypher
#find the frequency of each of the letter
#then correlate and match each letter to the frequency table
#try different combinations of letters to get closest match

###Algorithm###
#Access the frquescy table an
#LOOP: the frequency of each letter, the amount of letters
#Find the percentage of each
#Match percentages to the original table
#FUNCTION: Finding frequency of each
#FUNCTION: Finding percentages
#FUNCTION: Finding total number of letters
import string
import operator

freqtable = {"A": 8.12, "B": 1.49, "C": 2.71, "D": 4.32, "E": 12.02, "F": 2.30, "G": 2.03, "H": 5.92, "I": 7.31,
             "J": 0.10, "K": 0.69, "L": 3.98, "M": 2.61, "N": 6.95, "O": 7.68, "P": 1.82, "Q": 0.11, "R": 6.02,
             "S": 6.28, "T": 9.10, "U": 2.88, "V": 1.11, "W": 2.09, "X": 0.17, "Y": 2.11, "Z": 0.07}

def freqofeach(mystring):
    capstring = mystring.upper()
    letters = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0,
               "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
    for i in capstring:
        if i in letters:
            letters[i] += 1
    return letters


def numofletters(mystring):
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]
    lowerstring = mystring.lower()
    total = 0
    for i in lowerstring:
        if i in alpha:
            total += 1
    return total

def percfreq(freqs, total):
    percsdict = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0,
               "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
    for letter in freqs:
        perc = (freqs[letter] / total) * 100
        percsdict[letter] = perc
    return percsdict

def main():
    mostfreq = ["E", "T", "A", "O", "I", "N", "S", "H", "R", "D", "L", "C", "U", "M", "W", "F", "G", "Y", "P", "B", "V",
                "K", "J", "X", "Q", "Z"]
    thestring = "tivzgylyrdroohvmwblfgsvzwwivhhdsvivblfszevglhvmwgsvnlmvbzmwblfdrootvggsvkilwfxg/gsvzwwivhhrhhvevmgsivvlmvlmvdsvvohyziildiwblfdroohvvzpvbkzwlmgsvwllivmgvigsvhvxivgpvblmvlmvulfigdlzmwgsvwllidroolkvmblfdroonvvggsvylhhgsviv"
    decode = ""
    upperstring = thestring.upper()
    frequencies = freqofeach(thestring)
    totals = numofletters(thestring)
    percentages = percfreq(frequencies, totals)
    mylist = []
    alphalist = []
    sorted_x = sorted(percentages.items(), key=operator.itemgetter(1))
    for item in sorted_x[::-1]:
        mylist.append(item)
    for thing in mylist:
        alphalist.append(thing[0])

    for letter in upperstring:
        if letter in mostfreq:
            index = alphalist.index(letter)
            decode += mostfreq[index]

    print(decode)
    #for key in percentages:




main()
#print(freqofeach("tivzgylyrdroohvmwblfgsvzwwivhhdsvivblfszevglhvmwgsvnlmvbzmwblfdrootvggsvkilwfxg/gsvzwwivhhrhhvevmgsivvlmvlmvdsvvohyziildiwblfdroohvvzpvbkzwlmgsvwllivmgvigsvhvxivgpvblmvlmvulfigdlzmwgsvwllidroolkvmblfdroonvvggsvylhhgsviv"))