# Might be better to make the question a bigger scope so you cant jut brute force it
data = input().split(' ')
number = int(data[0])+int(data[1])

if number in [2,3,5,7,11,13,17,19,23,29,31,37,41,43] and int(data[0]) in [1, 3, 4, 5, 7, 9, 10]: # 12+31=43 Max number
    print('Planting Day!')
else:
    print('No planting today.')

