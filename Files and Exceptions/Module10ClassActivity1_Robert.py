#Robert Bayer
#Module 10 Class Activity 1

#1
#   read() opens the file for the program to be able to extract the data for usage
#   readline() has the program read th the entire file into a list to be able to extract the data from.e file one line at a time to extract the data
#   readlines() has the program load
#2
import sys
mode = 'r' # read mode
filename = "values.txt"
total = 0


try:
    inputFileObj = open(filename, mode)

    for line in inputFileObj:
        total += int( line )
    print('Total of the values in', filename, 'is', total)

except:
    print( 'ERROR! Unable to open or read', filename)
    sys.exit()

inputFileObj.close()


#3
import sys

filename = "letters.txt"
mode = 'r'  # read mode

try:
    inputFileObj = open( filename, mode)

    for line in inputFileObj:
        line = inputFileObj.readline()
        print(line, end='')

except:
    print("ERROR! Unable to open or read", filename)
    sys.exit()
finally:
    inputFileObj.close()
#   It will print every other letter of the alphabet starting with "B" because the for loop reads one line, then the line defining the line variable asks the program to read the next line.