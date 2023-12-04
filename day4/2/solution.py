import re

f = open("day4/1/input.txt")
sum = 0
copies = {i:1 for i in range(200)}
for index, line in enumerate(f):
    index_string, nbrstot = line.split(':')
    winning_nbrs, gotten_nbrs = nbrstot.split('|')
    win_list = [int(item.group()) for item in re.finditer("\d+", winning_nbrs)]
    get_list = [int(item.group()) for item in re.finditer("\d+", gotten_nbrs)]
    #print(copies[index])
    value = 0
    for nbr in get_list:
        for winnbr in win_list:
            if nbr == winnbr:
                value +=1
    for i in range(copies[index]):
        sum += 1
        #print("value: " + str(value))
        for i in range(value):
            #print("adding copy for index: " + str(index + i + 1))
            copies[index + i + 1] += 1
f.close()
print(sum)