file = open("./day4", "r")
array = []
for line in file:
    array.append(line)

count = 0
for x in range(len(array)):
    for y in range(len(array[x])):
        if array[x][y] != "X":
            continue
        for h in range(-1, 2):
            for v in range(-1, 2):
                if v == 0 and h == 0:
                    continue
                if x + h * 3 < 0 or x + h * 3 >= len(array) or y + v * 3 < 0 or y + v * 3 >= len(array[0]):
                    continue
                if array[x + h][y + v] == "M" and array[x + 2 * h][y + 2 * v] == "A" and array[x + 3 * h][y + 3 * v] == "S":
                    count += 1

print(count)
