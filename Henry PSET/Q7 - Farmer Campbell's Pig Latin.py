# add upper case and punctuation to make harder?
# then add "ay" add to the end of the word

sentence = input().split(' ')
piggy = []

for word in sentence:
    if list(word)[0] in list('aoeiu'):
        piggy.append(word+'way')
    else:
        for letter in word:
            word = list(word)
            if letter not in list('aoeiu'):
                word.remove(letter)
                word.append(letter)
            else:
                piggy.append(''.join(word)+'ay')
                break
            


piggy = ' '.join(piggy)
print(piggy)

