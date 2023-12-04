import re

f = open("day2/1/input.txt")
outfile = open("day2/1/output.txt", 'w')
colours = {'red': 12, 'green': 13, 'blue': 14}
sum = 0
i = 0
for line in f:
    index_regex = re.search(" .*\:", line)
    subsets = re.findall(" [0-9].*?;| [0-9].*?\Z| [0-9].*?\n", line[index_regex.end():])
    max_counts = {'red': 0, 'green': 0, 'blue': 0}
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
                    if int(amount) > max_counts[colour]:
                        max_counts[colour] = int(amount)
                    #print(amount)
    partsum = 1
    for c in max_counts:
        partsum *= max_counts[c]
    sum += partsum
    i += 1
    # if(i > 1):
    #     break
f.close()
outfile.close()
print(sum)