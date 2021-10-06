#Robert Bayer
#Lab 17


#Removes a given letter from the entire sentence
def remove_letter(sentence, letter):
    new = ""
    for i in sentence:
        if i != letter:
            new += i
    return new

#Replaces a give word with another given word
def replace_word(sentence, target, replacement):
    x = sentence.find(target)
    y = len(target)
    y = x + y
    new = sentence[:x-1] + " " + replacement + " " + sentence[y+1:]
    return new

#Reverses the order of the words in a sentence
def reverse_sentence(sentence):
    new = ""
    word = ""
    x = 0
    y = len(sentence)-1
    for i in sentence:
        if i == " ":
            new = word + " " + new
            word = ""
        else:
            word += i
        if x == y:
            new = word + " " + new
        x += 1

    return new

#The main working function
def main():
    x = input("Input the message you want cut up: ")
    r = input("What letter do you want removed: ")
    w = input("Give me a word you want to replace: ")
    f = input("Give me a word you want to replace it with: ")
    print(remove_letter(x, r))
    print(replace_word(x, w, f))
    print(reverse_sentence(x))

#Calling the main working function
main()