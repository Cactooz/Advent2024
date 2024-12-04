file = open("./day4", "r")
array = []
for line in file:
    array.append(line)

count = 0
for x in range(1, len(array) - 1):
    for y in range(1, len(array[x]) - 1):
        if array[x][y] != "A":
            continue
        if (array[x - 1][y - 1] == "M" and array[x + 1][y + 1] == "S" and array[x - 1][y + 1] == "M" and array[x + 1][y - 1] == "S"
        ) or (array[x - 1][y - 1] == "S" and array[x + 1][y + 1] == "M" and array[x - 1][y + 1] == "S" and array[x + 1][y - 1] == "M"
        ) or (array[x - 1][y - 1] == "M" and array[x + 1][y + 1] == "S" and array[x - 1][y + 1] == "S" and array[x + 1][y - 1] == "M"
        ) or (array[x - 1][y - 1] == "S" and array[x + 1][y + 1] == "M" and array[x - 1][y + 1] == "M" and array[x + 1][y - 1] == "S"):
            count += 1

print(count)
