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

# Print 5 most frequent words
sorted_di = sorted([(v,k) for k,v in di.items()], reverse = True)
print([(k, v) for v,k in sorted_di[:5]])

# Equivalently:
tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)

# print("Flipped", tmp)

tmp = sorted(tmp, reverse = True)
# print("Sorted", tmp[:5])

for v,k in tmp[:5]:
    print(k, v)
