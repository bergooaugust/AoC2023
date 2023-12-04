f = open("day1/1/input.txt")
outfile = open("day1/2/output.txt", 'w')
numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

sum = 0
for line in f:
    digits = ""
    for index, char in enumerate(line):
        if char.isdigit():
            digits += char
            break
        else:
            foundnbr = False
            for number in numbers:
                if index + len(number) > len(line):
                    break
                if line[index:(index + len(number))] == number:
                    digits += str(numbers[number])
                    foundnbr = True
                    break
            if foundnbr:
                break
    revline = line[::-1]
    for index, char in enumerate(revline):
        if char.isdigit():
            digits += char
            break
        else:
            foundnbr = False
            for number in numbers:
                if index + len(number) > len(line):
                    break
                if revline[index:(index + len(number))] == number[::-1]:
                    digits += str(numbers[number])
                    foundnbr = True
                    break
            if foundnbr:
                break
    outfile.write(digits + '\n')
    sum += int(digits)
print(sum)
f.close()
outfile.close()