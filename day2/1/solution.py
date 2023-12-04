import re

f = open("day2/1/input.txt")
outfile = open("day2/1/output.txt", 'w')
colours = {'red': 12, 'green': 13, 'blue': 14}
sum = 0
i = 0
for line in f:
    possible = True
    index_regex = re.search(" .*\:", line)
    subsets = re.findall(" [0-9].*?;| [0-9].*?\Z| [0-9].*?\n", line[index_regex.end():])
    for subset in subsets:
        amounts = {'red': 0, 'green': 0, 'blue': 0}
        setcolours = re.findall("[0-9].*?,|[0-9].*?;|[0-9].*?\Z|[0-9].*?\n", subset)
        for c in setcolours:
            amount = re.match("[0-9]* ", c).group()
            if i == 84:
                print(amount)
            for colour in colours:
                if len(re.findall(colour, c)) > 0:
                    amounts[colour] = int(amount)
                    #print(amount)
        for a in amounts:
            if(i == 84):
                for s in setcolours:
                     print(s)
                print(str(amounts[a]) + " is the amount")
                print("checking against " + str(colours[a]))
            if amounts[a] > colours[a]:
                possible = False
    if possible:
        print(index_regex.group()[1:-1] + " POSSIBLE")
        sum += int(index_regex.group()[1:-1])
    else:
        print("IMPOSSIBLE")
    i += 1
    # if(i > 1):
    #     break
f.close()
outfile.close()
print(sum)