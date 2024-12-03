file = open("./day2", "r")

safeCount = 0
safeCountDampened = 0

def safe(numbers):
    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    return (all(1 <= abs(diff) <= 3 for diff in diffs) and
            (all(diff >= 0 for diff in diffs) or all(diff <= 0 for diff in diffs)))

for line in file:
    numbers = list(map(int, line.strip().split()))

    if safe(numbers):
        safeCount += 1
        continue

    for index in range(len(numbers)):
        dampenedNumbers = numbers[:index] + numbers[index + 1:]
        if safe(dampenedNumbers):
            safeCountDampened += 1
            break

print(safeCount)
print(safeCount + safeCountDampened)
