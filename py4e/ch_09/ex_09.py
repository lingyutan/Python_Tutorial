fname = input('Enter File:')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.strip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1

largest = -1
theword = None

for k,v in di.items():
    if v > largest:
        largest = v
        theword = k

print(theword, largest)
