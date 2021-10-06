#Robert Bayer
#Lab 22
#Takes a file name and sorts all lines in alphabetical

def sortafile(filename):
    try:
        FileObj = open(f"{filename}.txt", "r")
        OutputFileObj = open(f"{filename}Sorted.txt", "w")
        linelist = FileObj.readlines()
        linelist.sort()

        for item in linelist:
            OutputFileObj.write(item)

        FileObj.close()
        OutputFileObj.close()

    except Exception as e:
        print(e)
        print("You request is not able to be processed right now...")

def main():
    Writing = open("quotes.txt", "w")
    Writing.write(""""It’s not my fault." – Han Solo
"Your focus determines your reality." – Qui-Gon Jinn
"Do. Or do not. There is no try." – Yoda
"Somebody has to save our skins." – Leia Organa
"In my experience there is no such thing as luck." – Obi-Wan Kenobi
"I find your lack of faith disturbing." – Darth Vader
"I’ve got a bad feeling about this." – basically everyone
"It’s a trap!" – Admiral Ackbar
"So this is how liberty dies…with thunderous applause." – Padmé Amidala
"Your eyes can deceive you. Don’t trust them." – Obi-Wan Kenobi
"Never tell me the odds." – Han Solo
"Mind tricks don’t work on me." – Watto
"Great, kid. Don’t get cocky." – Han Solo
"Stay on target." – Gold Five
"This is a new day, a new beginning." – Ahsoka Tano""")
    Writing.close()
    sortafile("quotes")

main()