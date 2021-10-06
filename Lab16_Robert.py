#Lab 16
#Author: Robert

#Divides the string into two halfs and returns both halves as a duple
def half(string):
    even = ""
    odd = ""
    for i in range(0, len(string)):
        if i % 2 == 0:
            even += string[i]
        else:
            odd += string[i]
    return even, odd

#Takes the two halves and puts them back together in proper order
def together(x, y):

    alltogether = ""

    if len(x) > len(y):
        for i in range(0, len(y)):
            alltogether += x[i]
            alltogether += y[i]
        alltogether += x[len(x)-1]
        return alltogether
    else:
        for i in range(0, len(x)):
            alltogether += x[i]
            alltogether += y[i]
        return alltogether

#Main function
def main():
    x = input("Enter String: ")
    evenhalf = half(x)[0]
    oddhalf = half(x)[1]
    print(f'the first half is "{evenhalf}" and the second half is "{oddhalf}"')
    print(f'Putting them together now looks like: "{together(evenhalf, oddhalf)}"')

main()