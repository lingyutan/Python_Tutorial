
fh = open('mbox-short.txt')

for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        print(line)
    if line.startswith('From '):
        at = line.find('@')
        finish = line[at: ].find(' ')
        print("Email:", line[5 :at+finish])
