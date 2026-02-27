stops = int(input())

busses = []

for i in range(stops):
    busses.append(input())

fast = 0
slow = 0

for i in busses:
    i = i.split(' ')
    fast += int(i[1])

    slow += (int(i[0]) + int(i[1]))

print(fast, slow)
