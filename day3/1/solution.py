import numpy as np
import re
f = open("day3/1/input.txt")
outfile = open("day2/1/output.txt", 'w')
sum = 0
matrix = np.ones((140, 140))
numbers = []
for row_index, line in enumerate(f):
    for col_index, c in enumerate(line):
        if c == '.' or c.isdigit():
            matrix[row_index, col_index] = 0
    numbers += [re.finditer("[0-9]+", line)]

for row_index, number_line in enumerate(numbers):
    for number in number_line:
        start_index = number.start()
        end_index = number.end()
        added = False
        #search prev row
        if row_index > 0 and not added:
            for i in range(max(start_index - 1, 0), min(end_index + 1, 140)):
                if matrix[row_index - 1, i] == 1:
                    added = True
                    break
        #search this row
        if not added:
            for i in range(max(start_index - 1, 0), min(end_index + 1, 140)):
                if matrix[row_index, i] == 1:
                    added = True
                    break
        #search next row
        if row_index < 139 and not added:
            for i in range(max(start_index - 1, 0), min(end_index + 1, 140)):
                if matrix[row_index + 1, i] == 1:
                    added = True
                    break
        if added:
            sum += int(number.group())
            print("added " + number.group())
f.close()
outfile.close()
print(sum)