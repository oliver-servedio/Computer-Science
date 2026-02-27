input()
date = input()                    # Makes input str
                                  # Last Character in date

if date[-1] in list('4567890'):
    print('Yes')
elif date in ('11', '12', '13', '14'):      # Checks edge cases
    print('Yes')
else:
    print('No')