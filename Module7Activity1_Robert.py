#Robert Bayer
#Module 7 Class Activity 1

def make_list(a,b):
    if a > b:
        for i in range(b, a+1):
            print(i)
    elif a < b:
        for i in range(a, b+1):
            print(i)
    else:
        print("Invalid Entry, numbers cannot be equal")

        num_one = int(input("Enter a number: "))
        num_two = int(input("Enter another number: "))

        make_list(num_one, num_two)

num_one = int(input("Enter a number: "))
num_two = int(input("Enter another number: "))

make_list(num_one,num_two)

def make_sum(a,b):
    num = 0
    if a > b:
        for i in range(b,a+1):
            num += i
        print(num)
    elif a < b:
        for i in range(a,b+1):
            num += i
        print(num)
    else:
        print(a)

sum_one = int(input("Enter a number: "))
sum_two = int(input("Enter another number: "))

make_sum(sum_one,sum_two)