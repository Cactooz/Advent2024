import re

file = open("./day3", "r")

mulSum = 0
apply = True
for line in file:
    matches = re.findall("mul\(\d+,\d+\)|don't\(\)|do\(\)", line)
    for match in matches:
        if match == "don't()":
            apply = False
            continue
        elif match == "do()":
            apply = True
            continue

        if apply:
            parts = re.findall("\d+", match)
            mulSum += int(parts[0]) * int(parts[1])

print(mulSum)
