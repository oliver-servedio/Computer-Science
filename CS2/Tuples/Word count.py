import string
fhand = open(r"C:\Users\oservedio27\Desktop\Comp Sci\CS2\Tuples\Tuples.txt", 'r')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            if letter.isalpha():
                # Either adds to dict or makes new
                if letter not in counts:
                    counts[letter] = 1
                else:
                    counts[letter] += 1

# Sort the dictionary by value
lst = list()

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)

# Code: https://www.py4e.com/code3/count3.py