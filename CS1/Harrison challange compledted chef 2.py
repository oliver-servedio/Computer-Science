inputt = input('what are your numbers? ')
my_list = inputt.split(',')
n = int(my_list[1])
c = float(my_list[0])
amount = -1
final = 0
while n > 0:
    t = int(my_list[amount])
    final += (((t*t)/100)*0.01*c*18)
    n -= 1
    amount -= 1
print(int(final)+1)
