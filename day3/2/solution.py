import numpy as np
import re
f = open("day3/1/input.txt")
outfile = open("day2/1/output.txt", 'w')
sum = 0
numbers = np.zeros((140, 140))
gears = []
for row_index, line in enumerate(f):
    gears += [(row_index, re.finditer("\*", line))]
    for num in re.finditer("[0-9]+", line):
        numbers[row_index, num.start():num.end()] = int(num.group())
for row_index, geariter in gears:
    for gear in geariter:
        gear_col = gear.start()
        terms = []
        if row_index > 0:
            terms += list(dict.fromkeys(numbers[row_index - 1, (gear_col-1):(gear_col+2)]))
        terms += list(dict.fromkeys(numbers[row_index, (gear_col-1):(gear_col+2)]))
        if row_index < 139:
            terms += list(dict.fromkeys(numbers[row_index + 1, (gear_col-1):(gear_col+2)]))
        multerms = []
        for term in terms:
            if term > 0:
                multerms += [term]
        
        #print(multerms)
        if len(multerms) == 2:
            sum += multerms[0] * multerms[1]
            print("added " + str(multerms[0]) + " * " + str(multerms[1]))
        #print(gear.group() + str(row_index))
    
    # for number in number_line:
    #     start_index = number.start()
    #     end_index = number.end()
    #     added = False
    #     #search prev row
    #     if row_index > 0 and not added:
    #         for i in range(max(start_index - 1, 0), min(end_index + 1, 140)):
    #             if matrix[row_index - 1, i] == 1:
    #                 added = True
    #                 break
    #     #search this row
    #     if not added:
    #         for i in range(max(start_index - 1, 0), min(end_index + 1, 140)):
    #             if matrix[row_index, i] == 1:
    #                 added = True
    #                 break
    #     #search next row
    #     if row_index < 139 and not added:
    #         for i in range(max(start_index - 1, 0), min(end_index + 1, 140)):
    #             if matrix[row_index + 1, i] == 1:
    #                 added = True
    #                 break
    #     if added:
    #         sum += int(number.group())
    #         print("added " + number.group())
f.close()
outfile.close()
print(sum)