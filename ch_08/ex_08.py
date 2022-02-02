han = open('mbox-short.txt')

for line in han:
    line = line.strip()
    wds = line.split()
    # guardian in a compound statement, short circuit evaluation
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
