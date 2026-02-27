
x = input()
x = x.split(' ')

bus_number = int(x[0])

time_left = int(x[1])

bus_info = []

for i in range(bus_number):
    bus_info.append(input().split(' '))

T = 0
F = 0
for i in range(len(bus_info)):
    T += int((bus_info[i])[1])
    F += int(((bus_info[i])[0]))
# print(bus_info)
# final = ((time_left - int((bus_info[0])[1]))/(int((bus_info[0])[0])))

final = (time_left - T)/F
if final < 0:
    final = 0
if final > 1:
    final = 1

print(final)


# 2 30 
# 7 10 
# 8 10

