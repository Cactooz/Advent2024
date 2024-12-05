file = open("./day5", "r")

def valid(pages):
    for i, page in enumerate(pages):
        if page not in order:
            continue
        for later_page in order[page]:
            if later_page in pages and pages.index(later_page) < i:
                return False
    return True

order = {}
line = file.readline()
while line != "\n":
    parts = line.strip().split("|")
    if parts[0] not in order:
        order[parts[0]] = []
    order[parts[0]].append(parts[1])

    line = file.readline()

middle_sum = 0

for line in file:
    parts = line.strip().split(",")
    if valid(parts):
        middle_sum += int(parts[len(parts) // 2])

print(middle_sum)
