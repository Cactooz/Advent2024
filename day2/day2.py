file = open("./day2", "r")

safeCount = 0

for line in file:
    numbers = list(map(int, line.strip().split()))
    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

    if (all(1 <= abs(diff) <= 3 for diff in diffs) and
            (all(diff >= 0 for diff in diffs) or all(diff <= 0 for diff in diffs))):
        safeCount += 1
        continue

print(safeCount)
