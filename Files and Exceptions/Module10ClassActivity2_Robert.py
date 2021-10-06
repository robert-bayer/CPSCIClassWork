#Robert Bayer
#Module 10 Class Activity 2


#1
try:
    FileObj = open("pythonOutput.txt" ,"w+")
    FileObj.write("Hello, world")
    FileObj.close()

except Exception as e:
    print(e)
    print("There was ann error writing the string...")


#2
InputFileName = "transactions.txt"
total = 0
name = ""

try:
    InputFileObj = open(InputFileName, "r")
    OutputFileObj = open("Summary.txt", "w+")
    aline = InputFileObj.readline()
    OutputFileObj.write(f"{aline}\n")

    while aline:
        if aline == "Deposit \n":
            aline = InputFileObj.readline()
            total += float(aline[:-2])
            print(total)
        elif aline == "Withdraw \n":
            aline = InputFileObj.readline()
            total -= float(aline[:-2])
            print(total)
        else:
            aline = InputFileObj.readline()

    OutputFileObj.write(str(total))

except Exception as l:
    print(l)
    print("There was an error calculating the summary")