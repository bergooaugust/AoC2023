f = open("day1/1/input.txt")

sum = 0
for line in f:
    digits = ""
    for char in line:
        if char.isdigit():
            digits += char
            break

    for char in reversed(line):
        if char.isdigit():
            digits += char
            break
    sum += int(digits)
print(sum)
f.close()