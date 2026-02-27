name = input()
fname = ''                          # Forward name
bname = []                          # Backward name
for letter in name:
    if letter.isalpha():
        letter = letter.lower()     # letter.lower() didn't work w/out the =
        fname += letter
        bname.insert(0, letter)

bname = ('').join(bname)
if bname == fname:
    print('No eggs for you!')
else:
    print('Here are your eggs!')