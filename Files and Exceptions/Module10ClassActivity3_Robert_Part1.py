#Robert Bayer
#Module 10 Class Activity 3

FileObj = open("studentdata.txt", "r")
OutputObj = open("failingstudents.txt", "w")
aline = FileObj.readline()

while aline:
    aline = aline.split()
    name = aline[0]
    del aline[0]
    if len(aline) < 8:
        OutputObj.write(f"{name}\n")
    aline = FileObj.readline()

FileObj.close()
OutputObj.close()