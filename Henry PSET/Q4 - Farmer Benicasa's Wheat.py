units = int(input())
cost = 0


if int(units) <= 1000:
    cost = 0
units -= 1000

if units <= 4000:
    cost = units * 0.1
else:
    cost += 4000 * 0.1
    units -= 4000

    if units <= 5000:
        cost += units * 0.15
    else:
        cost += 5000 * 0.15
        units -= 5000
        cost += units * 0.2         # Above 10000

print(int(cost))