import copy

x = input()
x = x.split(' ')

rooms = int(x[0])
doors = int(x[1])

info = []

for room in range(rooms):
   info.append(input())

for door in info:
    new_list = copy.deepcopy(info)
    print(info.index(door))
    new_list.pop(info.index(door))
    newest_list = []
    for i in new_list:
        i.split(' ')
        newest_list.append([i[0], i[1]])
    for i in range(2):
        if door[i] in newest_list[i]:
            info.pop(info[i])
            


            
