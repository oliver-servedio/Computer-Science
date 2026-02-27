

def classifyPlate(plate):

    final = []

    letters = list(plate[:3])
    numbers = list(plate[3:])

    print("Letters:", letters)
    print("Numbers:", numbers)
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers_list = list("0123456789")

    # Checks first Half of the alphabet
    if letters[0] in alphabet[:13] and letters[1] in alphabet[:13] and letters[2] in alphabet[:13]:
        final.append("B")

    # Checks second Half of the alphabet
    if letters[0] in alphabet[13:] and letters[1] in alphabet[13:] and letters[2] in alphabet[13:]:
        final.append("E")

    if alphabet.index(letters[0]) == (alphabet.index(letters[1]) +1) and (alphabet.index(letters[1]) +1) == (alphabet.index(letters[2]) +2):
        final.append("D")

    if (alphabet.index(letters[0]) + 2) == (alphabet.index(letters[1]) +1) and (alphabet.index(letters[1]) + 1) == alphabet.index(letters[2]):
        final.append("I")

    if numbers_list.index(numbers[0]) == (numbers_list.index(numbers[1]) +1) and (numbers_list.index(numbers[1]) +1) == (numbers_list.index(numbers[2]) +2) and (numbers_list.index(numbers[2]) + 2) == (numbers_list.index(numbers[3]) +3):
        ts = False
        if "D" in final:
            final.remove("D")
            ts = True
        if "D" not in final and ts != True:
            final.append("D")
        

    if (numbers_list.index(numbers[0]) + 2) == (numbers_list.index(numbers[1]) +1) and (numbers_list.index(numbers[1]) + 1) == numbers_list.index(numbers[2]) and (numbers_list.index(numbers[2])) == (numbers_list.index(numbers[3]) - 1):
        ts = False
        if "I" in final:
            final.remove("I")
            ts = True
        if "I" not in final and ts != True:
            final.append("I")
    if 'I' in final and 'D' in final:
        final.remove("I")
        final.remove("D")

    if letters[0] in list("ABCDEF") and letters[1] in list("ABCDEF") and letters[2] in list("ABCDEF"):
        final.append("H")

    if '8' not in numbers and '9' not in numbers:
        if numbers[0] != '0':
            final.append("O")

    if letters[0] == letters[2]:
        final.append("P")

    if numbers[0] == numbers[3] and numbers[1] == numbers[2]:
        if "P" not in final:
            final.append("P")
    
    for i in list(plate):
        if (list(plate)).count(i) > 1:
            final.append("R")
            break
    
    if int(numbers[0]) + int(numbers[1]) + int(numbers[2]) == int(numbers[3]):
        final.append("S")
    
    if int(numbers[0]) + int(numbers[1]) + int(numbers[3]) == int(numbers[2]):
        if "S" not in final:
            final.append("S")

    if int(numbers[0]) + int(numbers[2]) + int(numbers[3]) == int(numbers[1]):
        if "S" not in final:
            final.append("S")

    if int(numbers[1]) + int(numbers[2]) + int(numbers[3]) == int(numbers[0]):
        if "S" not in final:
            final.append("S")
    

    if final == []:
        final = "NONE"
    
    final.sort()
    final = ''.join(final)
    
    return final


print(classifyPlate("NPR9876"))