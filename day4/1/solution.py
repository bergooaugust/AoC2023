import re

f = open("day4/1/input.txt")
sum = 0
for line in f:
    index_string, nbrstot = line.split(':')
    index = int(re.search("[0-9]+", index_string).group())

    winning_nbrs, gotten_nbrs = nbrstot.split('|')
    win_list = [int(item.group()) for item in re.finditer("\d+", winning_nbrs)]
    get_list = [int(item.group()) for item in re.finditer("\d+", gotten_nbrs)]
    value = 0
    for nbr in get_list:
        for winnbr in win_list:
            if nbr == winnbr:
                value = max(1, value * 2)
    sum += value
f.close()
print(sum)