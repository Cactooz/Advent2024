import re

file = open("./day3", "r")

mulSum = 0
for line in file:
    matches = re.findall("mul\((\d+),(\d+)\)", line)
    for match in matches:
        mulSum += int(match[0]) * int(match[1])

print(mulSum)
