import string

fhand = open(r"C:\Users\oservedio27\Desktop\Comp Sci\CS2\Tuples\Tuples.txt", 'r')
counts = dict()

for line in fhand:
    line = line.lower()
    words = line.split()
    if len(words) > 0:
        if words[0] == 'from':
            word = words[5].split(':')
            word = word[0]
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

lst = list()
for val, key in list(counts.items()):
    lst.append((key, val))

lst.sort(reverse=True)

for val, key in lst[:10]:
    print(key, val)