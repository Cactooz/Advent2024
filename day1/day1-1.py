file = open("./day1", "r")

first = []
second = []

for line in file:
    numbers = line.strip().split("   ")
    first.append(numbers[0])
    second.append(numbers[1])

first.sort()
second.sort()

differenceSum = 0

for i in range(len(first)):
    differenceSum += abs(int(first[i]) - int(second[i]))

print(differenceSum)
