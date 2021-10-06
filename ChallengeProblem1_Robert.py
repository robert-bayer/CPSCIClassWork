def alphashift(message, i):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for j in message:
        if j not in alpha:
            answer += j
        else:
            shift = alpha.find(j)
            shift += i
            shift = shift % 26
            answer += alpha[shift]
    return answer

def main():
    message = input("Enter your encoded meesage: ")
    message = message.lower()

    for i in range(0,26):
        print(alphashift(message,i))

main()