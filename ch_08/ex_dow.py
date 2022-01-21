han = open('mbox-short.txt')

for line in han:
    line = line.strip()
    wds = line.split()
    # guardian a bit stronger, or we can split it into two if's
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
