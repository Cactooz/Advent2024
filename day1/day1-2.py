file = open("./day1", "r")

first = []
second = []

for line in file:
    numbers = line.strip().split("   ")
    first.append(numbers[0])
    second.append(numbers[1])

multipliedSum = 0

for i in range(len(first)):
    times = 0
    for j in range(len(second)):
        if first[i] == second[j]:
            times += 1
    multipliedSum += int(first[i]) * times

print(multipliedSum)
