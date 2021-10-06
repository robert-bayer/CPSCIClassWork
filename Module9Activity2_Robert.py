import random
def lowest():
    assignments = [88, 94, 81, 92, 80, 82, 84, 74, 83, 93]
    x = assignments[0]
    h = 0
    for i in assignments[1:]:
        if i < x:
            x = i
            h = assignments.index(i)
    del assignments[h]
    total = 0
    average = 0
    for k in assignments:
        total = total + k
    average = total / len(assignments)
    average = round(average, 2)
    print(average)
    assignments = assignments + [x]
    print(assignments)

def grades():
    grades = [81.9, 76.8, 77.4, 99.4, 66.2, 67.7, 69.7, 85.7, 92, 69.3, 71.3, 73.9]
    newgrades = []
    x = grades[0]
    for i in grades[1:]:
        if i < x:
            x = i
    y = 100 - x
    print(y)
    h = 0
    for k in grades:
        h = grades.index(k)
        newgrades = newgrades + [grades[h] + y]
    print(newgrades)

def die():
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = x + y
    return z

def sortdie(number):
    results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(number):
        total = die()
        store = total - 2
        results[store] += 1
    return results

def displayResults(results):
    for i in range(len(results)):
        print(i + 2, ":", results[i])


def main():
    number = int(input("Enter the amount of times you want to roll the die: "))
    displayResults(sortdie(number))

lowest()
grades()
main()