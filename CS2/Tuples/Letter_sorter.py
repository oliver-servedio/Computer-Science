import string

fhand = open(r"C:\Users\oservedio27\Desktop\Comp Sci\CS2\Tuples\Tuples.txt", 'r')
counts = dict()

for line in fhand:
    line = line.lower()
    words = line.split()
    if len(words) > 0:
        if words[0] == 'from':
            word = words[1]

        elif words[0] == 'received:':
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)